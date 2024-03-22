import sys

def get_environment_3_10(dsm_value):
    print(dsm_value)
    print(type(dsm_value))
    match dsm_value:
        case value if value in {"prod", "production"}:
            return "PROD"
        case "uat":
            return "UAT"
        case value if value in {"dev", "development"}:
            return "DEV"
        case "lab":
            return "LAB"
        case _:
            return "DID_NOT_READ_3_10"
        
def get_environment(dsm_value):
    if 'prod' in dsm_value:
        # print("PROD")
        return 'PROD'
    elif 'uat' in dsm_value:
        # print('UAT')
        return 'UAT'
    elif 'lab' in dsm_value:
        # print('LAB')
        return 'LAB'
    elif 'dev' in dsm_value:
        # print('DEV')
        return 'DEV'
    else:
        print("No prod/dev/uat/lab found in name.")
        return None


def main():
    # Check if the argument was passed
    if len(sys.argv) < 2:
        print("Usage: roles/get_post_vault_keys/scripts/env_setter.py <env>")
        sys.exit(1)
    
    # Get the environment value from the command line arguments
    environment = sys.argv[1]
    
    # Now you can use the environment variable as needed
    # print("Received environment:", environment)
    
    try:
        environment_value = get_environment(environment)
        print(environment_value)
    except SyntaxError:
        environment_value = get_environment_3_10(environment)
        print(environment_value)


if __name__ == "__main__":
    main()
