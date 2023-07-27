# Valid IP Addresses: https://leetcode.com/problems/validate-ip-address/

"""
The time complexity is O(1), because we are splitting the input string and validating each part, which takes constant time since the size of the input is limited by the structure of IP addresses.

The space complexity is also O(1), because we are using only a constant amount of space to store the parts of the IP address.
"""


def validIPAddress(IP):
    def isIPv4(s):
        try: return str(int(s)) == s and 0 <= int(s) <= 255
        except: return False

    def isIPv6(s):
        if len(s) > 4: return False
        try: return int(s, 16) >= 0 and s[0] != '-'
        except: return False

    if IP.count(".") == 3 and all(isIPv4(i) for i in IP.split(".")): 
        return "IPv4"
    if IP.count(":") == 7 and all(isIPv6(i) for i in IP.split(":")): 
        return "IPv6"
    return "Neither"


print(validIPAddress("172.16.254.1"))  # Expected output: "IPv4"
print(validIPAddress("2001:0db8:85a3:0:0:8A2E:0370:7334"))  # Expected output: "IPv6"
print(validIPAddress("256.256.256.256"))  # Expected output: "Neither"
print(validIPAddress("2001:0db8:85a3::8A2E:0370:7334"))  # Expected output: "Neither"