import sys

import csv

from db import conn, create_ips, create_domains, create_cases


def main():
    cases_parsed = []
    domains_parsed = []
    ips_parsed = []

    with open('dump.csv', encoding='cp1251') as csv_file:
        csv_file.readline()
        csv.field_size_limit(sys.maxsize)
        reader = csv.reader(csv_file, delimiter=';', quotechar='"')

        for ind, line in enumerate(reader):
            ind += 1

            try:
                ips, domain, url, organization, number, date = line
                ips_splt = ips.split('|')
                
                cases_parsed.append((ind, organization, number, date))

                for ip in ips_splt:
                    if ip is not None and ip != '':
                        ips_parsed.append((ip, ind))

                if domain is not None and domain != '':
                    domains_parsed.append((domain, ind))

            except Exception as e:
                print(e)
                print(line)
                return -1

        cursor = conn.cursor()

        create_cases(cursor, cases_parsed)
        print('Cases done')

        create_domains(cursor, domains_parsed)
        print('Domains done')

        create_ips(cursor, ips_parsed)
        print('Ips done')

        conn.commit()
        cursor.close()

    conn.close()

if __name__ == "__main__":
    main()
