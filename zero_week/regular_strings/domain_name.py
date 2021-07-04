"""
Write a function that when given a URL as a string, parses out just the domain name and returns it as a string.

For example:

domain_name("http://github.com/carbonfive/raygun") == "github"
domain_name("http://www.zombie-bites.com") == "zombie-bites"
domain_name("https://www.cnet.com") == "cnet"
"""
import re


def domain_extract(link):
    if "www" in link:
        domain = link.split('.')[1]
        print(domain)
        return domain
    else:
        domain = re.split('[/.]', link)[2]
        print(domain)
        return domain


domain_extract("https://www.zombie-bites.com")
