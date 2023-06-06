from package_dir import package


def main():
    print('inside main')
    package.function()


if __name__ == '__main__':
    # Only run the main function if this module is called as main module
    main()