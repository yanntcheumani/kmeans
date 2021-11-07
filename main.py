import argparse

from Management import Management

def main():
    manage = Management('data/jordan.jpg', 2, 15.0)
    manage.run()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--interfaces", default=True, type=bool)
    parser.add_argument("--path", type=str)
    main()
