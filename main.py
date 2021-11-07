import argparse

from Management import Management


def main(file_path: str, nbr_cluster: int, display_state: bool, nbr_convergence: int):
    manage = Management(file_path, nbr_cluster, nbr_convergence, display_state)
    manage.run()


def run_interfaces():
    pass


def check_params(args):
    if args.interfaces and args.path is None and args.nbr_cluster is None \
            and args.nbr_convergence is None and not args.display_state:
        run_interfaces()
        exit(0)
    elif not args.interfaces and args.path is not None and args.nbr_cluster is not None \
            and args.nbr_convergence is not None:
        main(args.path, args.nbr_cluster, args.display_state, args.nbr_convergence)
    else:
        print("wrong arguments passed")
        exit(84)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--interfaces", default=True, type=bool)
    parser.add_argument("--path", type=str, help="path to the image")
    parser.add_argument("--nbr_cluster", type=int, help="number if color in new image")
    parser.add_argument("--nbr_convergence", type=float, help="number of convergence between each cluster")
    parser.add_argument('--display_state', type=bool, help="display the state every each step", default=False)
    args = parser.parse_args()

    check_params(args)
