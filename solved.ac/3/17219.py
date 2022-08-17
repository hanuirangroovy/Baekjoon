import sys

n, m = map(int, sys.stdin.readline().split())

site_password = {}

for _ in range(n):
    site, password = sys.stdin.readline().split()
    site_password[site] = password

for _ in range(m):
    want_site = sys.stdin.readline().strip()
    print(site_password[want_site])