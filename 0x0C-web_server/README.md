0x0C-web_server
Tasks:

  0. Transfer a file to your server:-
    a Bash script that transfers a file from our client to a server

    Requirements:

      .Accepts 4 parameters
        - The path to the file to be transferred
        - The IP of the server we want to transfer - - the file to
        - The username scp connects with
        - The path to the SSH private key that scpuses
      .Display Usage: 0-transfer_file PATH_TO_FILE IP  USERNAME PATH_TO_SSH_KEY if less than 3 parameters passed
      .scp must transfer the file to the user home directory ~/
      .Strict host key checking must be disabled when using scp