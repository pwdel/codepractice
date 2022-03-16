# PDFScrape Project

The purpose of this project is to investigate what it takes to set up a pipeline that scrapes words and raw text from PDFs and puts them in a Machine Learning pipeline of some sort.

The language we will use for this is GoLang.

# Existing Tools

https://www.pdf-online.com/osa/extract.aspx

```
  X Pos   Y Pos Text
 134,68  685,58 Accelerating Network Receive Processing
 226,80  660,68 Intel I/O Acceleration Technology
 151,29  624,81 Andrew Grover
 145,40  606,88 Intel Corporation
 113,62  588,95 andrew.grover@intel.com
 354,12  624,81 Christopher Leech
 356,60  606,88 Intel Corporation
 310,47  588,95 christopher.leech@intel.com
  74,88  540,73 Abstract
  74,88  503,96 Intel
  99,59  504,32 R
  96,79  503,96 
 111,11  503,96 I/O Acceleration Technology (I/OAT) is
  74,88  489,52 a
  84,23  489,52 set
 101,55  489,52 of
 115,54  489,52 features
 157,42  489,52 designed
```

https://www.extractpdf.com/

```
Accelerating Network Receive Processing
Intel I/O Acceleration Technology

Andrew Grover
Intel Corporation

Christopher Leech
Intel Corporation

andrew.grover@intel.com

christopher.leech@intel.com

Abstract
R I/O Acceleration Technology (I/OAT) is
Intel
a set of features designed to improve network
performance and lower CPU utilization. This
paper discusses the implementation of Linux
support for the three features in the network
controller and platform silicon that make up
I/OAT. It also covers the bottlenecks in network
receive processing that these features address,
and describes I/OAT’s impact on the network
stack.

1

Introduction

As network technology has improved rapidly
over the past ten years, a significant gap has
opened between the CPU overhead for sending
and for receiving packets. There are two key
technologies that allow the sending of packets
to be much less CPU-intensive than receiving
packets.
```


# Databases of Sample PDF Libraries

https://github.com/tpn/pdfs
https://github.com/openpreserve/format-corpus/tree/master/pdfCabinetOfHorrors 

https://www.cs.cmu.edu/~aharley/rvl-cdip/ 

https://commoncrawl.org/2013/08/a-look-inside-common-crawls-210tb-2012-web-corpus/

https://bulkdata.uspto.gov/

# Rough Outline

```
# create dockerfile with Go based upon debian
# scrape pdf with a go library
# remove all characters and non-words
# deposit all words into a text file as one big long string with spaces
# tokenize the big blank document
# deposit the tokens into another text file in json format
# store tokenized words in postgres
```

# Work

## Setting Up the Environment

Golang Docker file