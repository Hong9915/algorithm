import sys
input=sys.stdin.readline

N,M=map(int,input().strip().split())

site_password={}
for _ in range(N):
    site,password=map(str,input().strip().split())
    site_password[site]=password

for _ in range(M):
    y=input().strip()
    print(site_password[y])