### QPM is QualiSystems Package Manager

Usage: 
```
python -m qpm action [additional arguments]
```

Examples: 

Pack a CloudShell shell 
```
python -m qpm pack --package_name vCenterShell
```

Pack a CloudShell shell as specific version
```
python -m qpm pack --package_name vCenterShell --version 1.0.21
```


Install package into QualiSystems CloudShell 
```
python -m qpm install --package_name vCenterShell
```

