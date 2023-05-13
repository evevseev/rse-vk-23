import argparse

from db import get_connection, get_blocked_ips_count, get_blocked_domains_count, get_cases_count, get_case, find_ip, \
    find_domain

parser = argparse.ArgumentParser(
    prog='Client for searching in Blocked Sites Dump')

parser.add_argument('--dbhost', help='DB host', required=True)
parser.add_argument('--dbport', help='DB port', default=5432, type=int)
parser.add_argument('--dbname', help='DB name', required=True)
parser.add_argument('--dbuser', help='DB user', required=True)
parser.add_argument('--dbpass', help='DB password', required=True)
parser.add_argument('-s', '--stats', help='Print blocked stats', default=False, type=bool)

parser.add_argument('-ip', help='IP search', required=False)
parser.add_argument('-domain', help='Domain search', required=False)

args = parser.parse_args()


def main():
    conn = get_connection(args.dbhost, args.dbport, args.dbname, args.dbuser, args.dbpass)
    cursor = conn.cursor()

    if args.stats:
        print('IPs blocked: ', get_blocked_ips_count(cursor))
        print('Domains blocked: ', get_blocked_domains_count(cursor))
        print('Total cases: ', get_cases_count(cursor))
        return

    if args.ip and args.domain:
        print('You can not search IP and Domain simultaneously')
        return

    entries: list[tuple]
    if args.ip:
        entries = find_ip(cursor, args.ip)
    else:
        entries = find_domain(cursor, args.domain)

    for data, org, case_num, date in entries:
        print(f' - {data}\t\t{org}\t\t{case_num}\t\t{date}')

    cursor.close()
    conn.close()


if __name__ == "__main__":
    main()
