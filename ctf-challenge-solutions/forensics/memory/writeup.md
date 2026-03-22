# Challenge Name: Ghost in the Machine

## Challenge Details
- **Category:** Forensics
- **Difficulty:** Medium
- **Tools Used:** Volatility 3

## Vulnerability Explanation
Memory forensics involves analyzing a volatile memory dump (.vmem, .raw, .mem) from a machine to identify running processes, malware, network connections, and sometimes passwords or flags residing in plain text within active application memory.

## Step-by-Step Solution
1. **Reconnaissance:** Provided with a memory dump named `stix.vmem`.
2. **Analysis:** Initiated Volatility 3. Determined the OS profile was Windows 7 using `windows.info`.
3. **Exploitation:** 
   - Listed active processes using `windows.pslist`.
   - Noticed a suspicious process: `notepad.exe`.
   - Used `windows.cmdline` to check what file was opened with notepad, identifying `Secret.txt`.
   - Dumped the memory space of `notepad.exe` using `windows.memmap.Memmap --pid <PID> --dump`.
4. **Post-Exploitation:** Ran `strings` over the dumped memory image and `grep`ped for "CTF{". Discovered the flag.

## Proof of Concept
```bash
# Check cmds.txt for the exact Volatility syntax used in this scenario.
```

## Flag Format Example
`CTF{m3m0ry_n3v3r_l1es}`

## Defensive Recommendations
- Avoid storing critical secrets in plain text memory for longer than necessary. Utilize secure strings/memory-wiping techniques where appropriate.
- From an incident response perspective, ensure systems are configured to allow memory captures using trusted endpoints solutions before shutting down compromised machines.
