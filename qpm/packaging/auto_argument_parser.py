from types import FunctionType
from argparse import ArgumentParser
import inspect
import sys


class AutoArgumentParser(object):
    def __init__(self, type_to_parse, program=None):
        self.type = type_to_parse
        self.program = program

    def parse_args(self):
        actions = self._get_actions()
        parser = ArgumentParser(prog=self.program)
        parser.add_argument('action', type=str, help='Action to perform', choices=actions)
        package_manager = self.type()

        args = parser.parse_args()
        action = args.action

        if action not in actions:
            print 'Action {0} is not supported'.format(action)
            parser.print_help()
            return
        method = getattr(package_manager, action)
        arguments = AutoArgumentParser._get_method_arguments(method)
        for argument in arguments:
            parser.add_argument('--' + argument, type=str, required=_is_required, nargs='?')
        args = parser.parse_args()
        method_params = {arg: getattr(args, arg) for arg in arguments}
        method(**method_params)

        if action not in actions:
            print 'Action {0} is not supported'.format(action)
            parser.print_help()
            return
        method = getattr(package_manager, action)
        arguments = AutoArgumentParser._get_method_arguments(method)
        for argument in arguments:
            parser.add_argument('--' + argument, type=str, required=True, nargs='?')
        args = parser.parse_args()
        method_params = {arg: getattr(args, arg) for arg in arguments}
        method(**method_params)


    @staticmethod
    def _is_required(method, arg_name):
        getargspec = inspect.getargspec(method)
        index = getargspec.args.index(arg_name)
        index_from_the_end = len(getargspec.args) - 1 - index
        # argument has default value and thus is not required
        if index_from_the_end < len(inspect.getargspec(method).defaults):
            return False
        return True

    @staticmethod
    def _get_method_arguments(method):
        return [a for a in inspect.getargspec(method).args if a != 'self']

    def _get_actions(self):
        return [x for x, y in self.type.__dict__.items() if type(y) == FunctionType and not str(x).startswith('_')]


