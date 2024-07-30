import site


def locate_site_packages():
    site_packages_dirs = site.getsitepackages()

    print("Location(s) of site-packages:")

    for path in site_packages_dirs:
        print(path)




if __name__ == "__main__":
    locate_site_packages()
