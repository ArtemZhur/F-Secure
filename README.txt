Hello,
Python 3.7.3
From command line type python3 main.py -c(put path configuration file) -l(put path log file)
Example python3 main.py -c config.json -l log.txt
For each target page you can set period to .json configuration file
CONFIG FILE STRUCTURE EXAMPLE


{
   "pages":[
       {
           "url":"http://google.com",
           "content":"search",
           "period":"5"
       },
       {
           "url":"http://bing.com",
           "content":"fuck",
           "period":"10"

       }
   ]

}
