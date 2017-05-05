# FIXED: Selecting Option #5 "Inter-Cat", gives a incorrectly ordered user input prompt. "Enter the FULL PATH to your PASSWORD DICTIONARY FILE: "

# FIXED: Hybrid and Reverse-Hybrid Attacks

# FIXED: Combinator Attacks. I confused the switch for Brute Force with Combinator. Combinator = 1, Brute Force (Mask) = 3

# **BUGGED: "Mask-Attack" or "Brute-Force" syntax is bugged. Reading the manual on hashcat right now**

Source: https://hashcat.net/wiki/doku.php?id=mask_attack

**Okay... so they use a lot of fancy terms to describe something simple, for example "optparse" but for hashcat to properly use a character set you can either use "-1" or full length wise... "--custom-charset1=CS"

And....**

"-1 charsets/special/Russian/ru_ISO-8859-5-special.hcchr"

**Just means**

"--custom-charset1=CS charsets/special/Russian/ru_ISO-8859-5-special.hcchr"

**Which is located in this folder: /usr/share/hashcat/charsets/

So I am guessing this is how its supposed to be done**

"hashcat -a 3 (charset switch) (charset hcchr file) (password length)"

**so if you type '?l' 5-times for password length, it means the password is five-letters long, and letters ONLY. To include numbers its**

"hashcat -a 3 (charset switch) (charset hcchr file) (number switch) (password length)"

**Where number switch = '?l?d'**

**But you see, WPA2-PSK by itself, requires the user to have EIGHT characters at a minimum. So we should start the menu at that. However, I am not gonna just number that to the maximum bits. I'd rather have the user input it themselves.**

**Yeesh that is one ugly documentation. But okay one way that works is..**

"hashcat -a 3 (hashfile) (pw length)" 

**which is letters ONLY. To include numbers its...**

"hashcat -a 3 (hashfile) (include numbers) (pw length)"

**So its**

"hashcat -a 3 (hashfile) ?l?d ?l?l?l?l?l?l"

**for a six-letter password with words and numbers**

**You can also specify a "mask". And you can find your preloaded mask files with "locate masks" in terminal**

"hashcat -a 3 (hash to attack) (mask_file.hcmask)"


**What worked?**

This command worked, which specified a six digit password of both letters and numbers:**

"hashcat -a3 -m 2500 /media/root/Data/HashCatConverted/hashcat_20170405-013557.cap-01.cap.hccapx ?l?d ?l?l?l?l?l?l"

**I should use the mask file method as a separate method** 

**This one worked too:**

"hashcat -a3 -1 charsets/special/Russian/ru_ISO-8859-5-special.hcchr -m 2500 /media/root/Data/HashCatConverted/hashcat_20170405-013557.cap-01.cap.hccapx ?l?d ?l?l?l?l?l?l"

**So its...

"hashcat -a 3 -1 (maskfile) -m (hash type) (hash file) (number switch) (password length)"

**But there are four types of charset switches. This will need to be placed on hiatus until I get down ALL of it.

** Trying to Implement this interactive hash selection menu but...** 

THere appears to be... over 230 different types of hashes. They can be easily organized however. The -m made no sense anyways but Its easy for me to reorganize it alphabetically and categorize them.

Okay. So this requires a lot of organization. Because the crypto types are all over the place in the Hashcat help menu. However, we can just create a multi-tiered menu with several dicts in each. The dict formats should indicate what layer. For example

SHA_menu_layer_1()
-->SHA 1 types
-->SHA 256 Types
-->SHA 512 Types

And then, it should get more "specific"
 for example
 
 SHA_Menu_layer_1() --> SSHA_layer_2() --> LDAP (SSHA512)_layer_3()

OR menu #1, #2, #3 and so on.

So we can build the menus quickly, not using opt_List(), but instead have the python program run the 'cat' command on a text file. And the text file menus can be produced with spreadsheets with tables. That'll be easier and quicker.

That way, we can use it as a refererence, and the user just has to "Push button #1 ,2 3 etc."

# **Example Table of Layer #1** (Not Actual)
	Option Number	Encryption
Option #	1	MD (4, 5, HMAC PBKDF)
Option #	2	SHA (1, 256, 512, etc.)
Option #	3	GOST
Option #	4	DES (incl 3DES)
Option #	5	Skype
Option #	6	WPA/WPA2
Option #	7	CHAP
Option #	8	IKE-PSK
Option #	9	NTLM (incl NetNTLM)
Option #	10	Kerberos
Option #	11	DNSSEC
Option #	12	PostgresSQL
Option #	13	MS Office
Option #	14	Bitcoin
Option #	15	Blockchain
Option #	16	AIX
Option #	17	CISCO
Option #	18	MySQL
Option #	19	Winzip
Option #	20	Oracle
Option #	21	Apache
Option #	22	NSIDAPS
Option #	23	Blowfish
Option #	24	Windows Phone
Option #	25	Samsung Android
Option #	26	Grub
Option #	27	Aruba
Option #	28	SAP
Option #	29	Lotus
Option #	30	Peoplesoft
Option #	31	RAR
Option #	32	Winzip
Option #	33	LUKS
Option #	34	PDF
Option #	35	Plaintext
Option #	36	aes

# Design characteristics (under the hood) of Menu:

1. Rapidly put together via Microsoft Excel + Texteditors.
2. Has a "dual-key" to value pair. That means, "either press 1 will get you WPA2-PSK encryption cracking, OR, you can just type 2500", either way the opt_Dict = {'1': 2500, '2500':2500}
3. At least a "two-layer" submenu to help users choose.
4. May require multiple python modules. To better visualize and debug. 
5. Probably better to start with the most common cryptos first, OR, we can just use word to format the strings for the dicts. Or excel. 
6. When using a spreadsheet to build a "super-massive dict" you can use the columns of a Excel holder to hold each symbol. Example
{
'Key':'Value',
}

Column 1 Column 2 Column 3 Column 4 Column5 Column 6 Column 7 Column 8

'	Key	'		:	'	Value	'	,


This definitely can't be sorted in one day, but we can later add curly brackets, colons, semicolons in there to make the process much quicker. 

And I got really important matters to do this morning. Ttyl all

