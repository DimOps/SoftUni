version = input()

version_control = version.split('.')
version_control = list(map(int, version_control))

if version_control[2] <= 8:
    version_control[2] += 1
	
elif version_control[2] == 9:
    version_control[2] = 0
	
    if version_control[1] <= 8:
        version_control[1] += 1
		
    elif version_control[1] == 9:
        version_control[1] = 0
        version_control[0] += 1

version_control = list(map(str, version_control))
new_version = '.'.join(version_control)

print(new_version)
