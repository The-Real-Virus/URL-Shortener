import os
import contextlib
import sys
import re
import pyperclip  # Install with: pip install pyperclip
try:
    from urllib.parse import urlencode
    from urllib.request import urlopen
except ImportError:
    from urllib import urlencode
    from urllib2 import urlopen
from colorama import Fore, Style  # Install with: pip install colorama

# Function to display banner
def show_banner():
    banner = r"""
                       ______
                    .-"      "-.
                   /  *ViRuS*   \
       _          |              |          _
      ( \         |,  .-.  .-.  ,|         / )
       > "=._     | )(_0_/\_0_)( |     _.=" <
      (_/"=._"=._ |/     /\     \| _.="_.="\_)
             "=._ (_     ^^     _)"_.="
                 "=\__|IIIIII|__/="
                _.="| \IIIIII/ |"=._
      _     _.="_.="\          /"=._"=._     _
     ( \_.="_.="     `--------`     "=._"=._/ )
      > _.="                            "=._ <
     (_/                                    \_)
 ____________________________________________________
 ----------------------------------------------------        
        #  URL-Shortener
        #  Author : The-Real-Virus
        #  https://github.com/The-Real-Virus
 ____________________________________________________
 ----------------------------------------------------
"""
    print(banner)

# Show banner at script startup
show_banner()

# Ask user for input
choice = input("\nPress 'y' to continue or 'n' to exit: ").strip().lower()

if choice == 'n':
    print("\nExiting the script. Goodbye!")
    exit()
elif choice == 'y':
    os.system('clear' if os.name == 'posix' else 'cls')  # Clear screen on Linux/Mac ('clear') or Windows ('cls')
else:
    print("\nInvalid choice. Exiting the script.")
    exit()

# URL validation regex
URL_REGEX = re.compile(
    r"^(https?://)?(www\.)?"
    r"[a-zA-Z0-9-]{1,63}(\.[a-zA-Z]{2,6}){1,2}(/.*)?$"
)

def make_tiny(url):
    """Shorten a URL using TinyURL API."""
    if not re.match(URL_REGEX, url):
        print(f"{Fore.RED}Invalid URL: {url}{Style.RESET_ALL}")
        return None

    request_url = f"http://tinyurl.com/api-create.php?{urlencode({'url': url})}"
    try:
        with contextlib.closing(urlopen(request_url)) as response:
            return response.read().decode("utf-8")
    except Exception as e:
        print(f"{Fore.RED}Error shortening URL: {e}{Style.RESET_ALL}")
        return None

def logo():
    logo = r"""

███████╗██╗  ██╗ ██████╗ ██████╗ ████████╗███████╗███╗   ██╗███████╗██████╗ 
██╔════╝██║  ██║██╔═══██╗██╔══██╗╚══██╔══╝██╔════╝████╗  ██║██╔════╝██╔══██╗
███████╗███████║██║   ██║██████╔╝   ██║   █████╗  ██╔██╗ ██║█████╗  ██████╔╝
╚════██║██╔══██║██║   ██║██╔══██╗   ██║   ██╔══╝  ██║╚██╗██║██╔══╝  ██╔══██╗
███████║██║  ██║╚██████╔╝██║  ██║   ██║   ███████╗██║ ╚████║███████╗██║  ██║
╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝
                                                                                                                                                         
"""
    print(logo)

def main():
    print(f"{Fore.CYAN}Welcome to the URL Shortener!{Style.RESET_ALL}")

    # Check if URLs are provided as arguments
    if len(sys.argv) > 1:
        urls = sys.argv[1:]
    else:
        urls = input(f"{Fore.YELLOW}Enter URL(s) (comma-separated): {Style.RESET_ALL}").split(",")

    urls = [url.strip() for url in urls if url.strip()]

    if not urls:
        print(f"{Fore.RED}No valid URLs provided!{Style.RESET_ALL}")
        return

    shortened_urls = []
    for url in urls:
        short_url = make_tiny(url)
        if short_url:
            shortened_urls.append(short_url)
            print(f"{Fore.GREEN}Shortened: {short_url}{Style.RESET_ALL}")

    # Copy to clipboard if at least one URL was shortened
    if shortened_urls:
        pyperclip.copy("\n".join(shortened_urls))
        print(f"{Fore.MAGENTA}Shortened URLs copied to clipboard!{Style.RESET_ALL}")

if __name__ == "__main__":
    logo()
    main()
