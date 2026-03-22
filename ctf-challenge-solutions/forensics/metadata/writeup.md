# Challenge Name: Hidden Exif

## Challenge Details
- **Category:** Forensics
- **Difficulty:** Easy
- **Tools Used:** Exiftool

## Vulnerability Explanation
Metadata is "data about data." Files, particularly images, PDFs, and Office documents, contain embedded metadata tags detailing creation dates, software used, camera configurations, and occasionally GPS location coordinates or user notes. Attackers can extract this information using specialized tools to perform reconnaissance or uncover hidden clues.

## Step-by-Step Solution
1. **Reconnaissance:** Provided with a `.jpg` file that appears to show a normal desk.
2. **Analysis:** Suspecting embedded metadata, used `exiftool` on Kali to inspect the image tags.
3. **Exploitation:** Ran `exiftool desk_photo.jpg`. Scanned through the Camera Model, Date/Time, and finally stumbled across the "User Comment" tag.
4. **Post-Exploitation:** The User Comment tag clearly contained the CTF flag.

## Proof of Concept
```bash
# Check tool-output.txt for the exact Exiftool readout in this challenge.
# Command: exiftool desk_photo.jpg | grep Comment
```

## Flag Format Example
`CTF{m3tadata_t3lls_a_t4l3}`

## Defensive Recommendations
- Sanitize metadata from sensitive files prior to publishing them publicly to avoid leaking GPS locations, user IDs, or software versions. Most operating systems offer built-in attributes-stripping tools, or developers can use specialized scripts during the deployment pipeline.
