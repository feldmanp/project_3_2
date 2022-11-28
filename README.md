# Crypto Portfolio Dashboard and Personal Tax Calculation


![](./Resources/README_cover_image.png)


<br>

# Overview: 

### A simple user interface (UI) that allows investors to input their salary, connect their trading accounts where the UI will automatically identify CGT events and pass total taxable income into our tax calculator (based on Australia’s progressive bracket tax structure).

<br>

<br>

## Context: Why do we need crypto income tax calculator ? 

<br>

>## The rise of blockchain technology, powering decentralised currencies known as ‘Cryptocurrencies’ has led to ~1bn people globally owning/investing in some form of it
>### (Editors Choice, 2022)

<br>


The challenge with this global trend is two-fold:

There is a particular concentration on new retail investors and it also;
Is challenging how government and financial agencies treat these investments in a tax context

<br>

Recent legislation in Australia has meant profit/loss from crypto investments is captured as a capital gain/loss (CGT) event as opposed to foreign currency gains.

For more information about cryptocurrent investment taxation, please visit: https://www.ato.gov.au/Individuals/Capital-gains-tax/





# Instructions and user story 
<br>


> ## “John has two income streams: he earns a $150k p.a. salary as a software engineer at Optiver, and earns income executing hundreds of ethereum trades each financial year. John wants to find a straightforward tool to find out his personal income tax based on Australian Taxation Regulations” 

<br>

### John's information:
<br>

Salary : **$ 150,000**

Ethereum Account Address: **0x8c70a175F86FB25ae3ADBD5F26E043D119565EB1**


<br>
<br>


## 1. Run **'streamlit run app.py'** in your terminal (IOS user) / command line (for Windows user), then copy the URL into your browser. 
![](./Resources/instruction_run_streamlit_in_terminal.png)

![](./Resources/instructions_streamlit_interface.png)


<br>

## 2. Input annual, pre-taxed salary on streamlit interface 

![](./Resources/instruction_input_salary.png)

<br>

## 3. Input our Ethereum account address 

![](./Resources/instruction_input_aacount.png)

## 4. View the results! 
<br>

### -   Daily portfolio view
### - Net income: income after tax
### - tax rate: tax rate based on total income 
### - Tax Paid: tax based based on total income

![](./Resources/instruction_view_results.png)

