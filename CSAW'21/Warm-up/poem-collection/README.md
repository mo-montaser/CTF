# CSAW CTF 2021

## poem-collection challenge


![0 image](https://myoctocat.com/assets/images/base-octocat.svg)

When I opened the website, I found the link "poems".

![1 image](https://myoctocat.com/assets/images/base-octocat.svg)

After clicking "poems", there was an error.
              
![2 image](https://myoctocat.com/assets/images/base-octocat.svg)              

As shown above, the error in file_get_content (PHP function) because the file name is empty.I chose one of the suggested files.

![3 image](https://myoctocat.com/assets/images/base-octocat.svg)

In the URL, there was a parameter called "poem" and its value was the file I'd chose. I decieded to test this parameter aginst LFI vulnerability. I changed the value of that parameter to "flag.txt". There was another error.

![4 image](https://myoctocat.com/assets/images/base-octocat.svg)

The error indicates that there is no such file in the current directory. So I tried to add "../" to flag.txt.
That worked fine and showed the flag. 

![5 image](https://myoctocat.com/assets/images/base-octocat.svg)





