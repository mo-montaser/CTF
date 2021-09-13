# CSAW CTF 2021

## poem-collection challenge


![0 image](https://raw.githubusercontent.com/mo-montaser/CTF/main/CSAW'21/Warm-up/poem-collection/screenshots/0.png)

When I opened the website, I found the link "poems".

![1 image](https://raw.githubusercontent.com/mo-montaser/CTF/main/CSAW'21/Warm-up/poem-collection/screenshots/1.png)

After clicking "poems", there was an error.
              
![2 image](https://raw.githubusercontent.com/mo-montaser/CTF/main/CSAW'21/Warm-up/poem-collection/screenshots/2.png)              

As shown above, the error in file_get_content (PHP function) because the file name is empty.I chose one of the suggested files.

![3 image](https://raw.githubusercontent.com/mo-montaser/CTF/main/CSAW'21/Warm-up/poem-collection/screenshots/3.png)

In the URL, there was a parameter called "poem" and its value was the file I'd chose. I decieded to test this parameter aginst LFI vulnerability. I changed the value of that parameter to "flag.txt". There was another error.

![4 image](https://raw.githubusercontent.com/mo-montaser/CTF/main/CSAW'21/Warm-up/poem-collection/screenshots/4.png)

The error indicates that there is no such file in the current directory. So I tried to add "../" to flag.txt.
That worked fine and showed the flag. 

![5 image](https://raw.githubusercontent.com/mo-montaser/CTF/main/CSAW'21/Warm-up/poem-collection/screenshots/5.png)





