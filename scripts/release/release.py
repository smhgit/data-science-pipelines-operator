import argparse
import os

from params import params
from version_doc import version_doc


def env_opts(env: str):
    if env in os.environ:
        return {'default': os.environ[env]}
    else:
        return {'required': True}


def main():
    parser = argparse.ArgumentParser(
        description="DSP Release Tools."
    )

    subparsers = parser.add_subparsers(help='sub-command help', required=True)

    # Params.env generator inputs
    parser_params = subparsers.add_parser('params', help='Params.env generator inputs')
    parser_params.set_defaults(func=params)
    parser_params.add_argument('--tag', type=str, required=True, help='Tag for which to fed image digests for.')
    parser_params.add_argument('--quay_org', default="opendatahub-io", type=str,
                               help='Tag for which to fed image digests for.')
    parser_params.add_argument('--out_file', default='params.env', type=str, help='File path output for params.env')
    parser.add_argument("--ubi-minimal", dest="ubi_minimal_tag", default="8.8",
                        help="ubi-minimal version tag in rh registry")
    parser.add_argument("--ubi-micro", dest="ubi_micro_tag", default="8.8",
                        help="ubi-micro version tag in rh registry")
    parser.add_argument("--mariadb", dest="mariadb_tag", default="1",
                        help="mariadb version tag in rh registry")
    parser.add_argument("--oauthproxy", dest="oauth_proxy_tag", default="v4.10",
                        help="oauthproxy version tag in rh registry")

    # Version Compatibility Matrix doc generator
    parser_vd = subparsers.add_parser('version_doc', help='Version Compatibility Matrix doc generator')
    parser_vd.set_defaults(func=version_doc)
    parser_vd.add_argument('--out_file', default='compatibility.md', type=str, help='File output for markdown doc.')
    parser_vd.add_argument('--input_file', default='compatibility.yaml', type=str,
                           help='Yaml input for compatibility doc generation.')

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
