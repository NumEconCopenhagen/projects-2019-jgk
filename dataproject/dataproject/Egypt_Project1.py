{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Project - Egypt's GDP and Unemployment"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The purpose of this project is to look into the if unemployment has an effect the on development of GDP. To help looking into this, Okun's Law is included in the thesis. Okun's law states that for each 1 % increase in unemployment, a country's GDP is going to be roughly 2 % lower than its potential GDP. In this study it will be looked into, how the unemployment rates acts to the trend we see for GDP. We will be looking at Egypt's GDP and unemployment rates from 1991 to 2014."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Part 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 245,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Importing Packages"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 246,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "from pandas_datareader import wb\n",
    "import wbdata\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "from matplotlib_venn import venn2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 247,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Importing data for Egypt's GDP from World Bank, 1991-2014"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 248,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>country</th>\n",
       "      <th>year</th>\n",
       "      <th>gdp</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Egypt, Arab Rep.</td>\n",
       "      <td>2014</td>\n",
       "      <td>2608.260442</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Egypt, Arab Rep.</td>\n",
       "      <td>2013</td>\n",
       "      <td>2590.945457</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Egypt, Arab Rep.</td>\n",
       "      <td>2012</td>\n",
       "      <td>2593.112377</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Egypt, Arab Rep.</td>\n",
       "      <td>2011</td>\n",
       "      <td>2593.214102</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Egypt, Arab Rep.</td>\n",
       "      <td>2010</td>\n",
       "      <td>2602.479549</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>Egypt, Arab Rep.</td>\n",
       "      <td>2009</td>\n",
       "      <td>2524.381342</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>Egypt, Arab Rep.</td>\n",
       "      <td>2008</td>\n",
       "      <td>2456.687446</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>Egypt, Arab Rep.</td>\n",
       "      <td>2007</td>\n",
       "      <td>2333.454571</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>Egypt, Arab Rep.</td>\n",
       "      <td>2006</td>\n",
       "      <td>2217.433320</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>Egypt, Arab Rep.</td>\n",
       "      <td>2005</td>\n",
       "      <td>2112.723735</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>Egypt, Arab Rep.</td>\n",
       "      <td>2004</td>\n",
       "      <td>2059.749606</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "             country  year          gdp\n",
       "0   Egypt, Arab Rep.  2014  2608.260442\n",
       "1   Egypt, Arab Rep.  2013  2590.945457\n",
       "2   Egypt, Arab Rep.  2012  2593.112377\n",
       "3   Egypt, Arab Rep.  2011  2593.214102\n",
       "4   Egypt, Arab Rep.  2010  2602.479549\n",
       "5   Egypt, Arab Rep.  2009  2524.381342\n",
       "6   Egypt, Arab Rep.  2008  2456.687446\n",
       "7   Egypt, Arab Rep.  2007  2333.454571\n",
       "8   Egypt, Arab Rep.  2006  2217.433320\n",
       "9   Egypt, Arab Rep.  2005  2112.723735\n",
       "10  Egypt, Arab Rep.  2004  2059.749606"
      ]
     },
     "execution_count": 248,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "gdp_wb = wb.download(indicator='NY.GDP.PCAP.KD', country=['EG'], start=1991, end=2014)                \n",
    "gdp_wb = gdp_wb.rename(columns = {'NY.GDP.PCAP.KD':'gdp'})\n",
    "gdp_wb = gdp_wb.reset_index()\n",
    "gdp_wb.year = gdp_wb.year.astype(int)\n",
    "gdp_wb.head(11)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The trend of GDP is seen to be overall increasing, however a smaller relative increase the last few years"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 249,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>country</th>\n",
       "      <th>year</th>\n",
       "      <th>gdp_growth</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Egypt, Arab Rep.</td>\n",
       "      <td>2014</td>\n",
       "      <td>2.915912</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Egypt, Arab Rep.</td>\n",
       "      <td>2013</td>\n",
       "      <td>2.185466</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Egypt, Arab Rep.</td>\n",
       "      <td>2012</td>\n",
       "      <td>2.226200</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Egypt, Arab Rep.</td>\n",
       "      <td>2011</td>\n",
       "      <td>1.764572</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Egypt, Arab Rep.</td>\n",
       "      <td>2010</td>\n",
       "      <td>5.147235</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>Egypt, Arab Rep.</td>\n",
       "      <td>2009</td>\n",
       "      <td>4.673600</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>Egypt, Arab Rep.</td>\n",
       "      <td>2008</td>\n",
       "      <td>7.156284</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>Egypt, Arab Rep.</td>\n",
       "      <td>2007</td>\n",
       "      <td>7.087827</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>Egypt, Arab Rep.</td>\n",
       "      <td>2006</td>\n",
       "      <td>6.843838</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>Egypt, Arab Rep.</td>\n",
       "      <td>2005</td>\n",
       "      <td>4.471744</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>Egypt, Arab Rep.</td>\n",
       "      <td>2004</td>\n",
       "      <td>4.092072</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "             country  year  gdp_growth\n",
       "0   Egypt, Arab Rep.  2014    2.915912\n",
       "1   Egypt, Arab Rep.  2013    2.185466\n",
       "2   Egypt, Arab Rep.  2012    2.226200\n",
       "3   Egypt, Arab Rep.  2011    1.764572\n",
       "4   Egypt, Arab Rep.  2010    5.147235\n",
       "5   Egypt, Arab Rep.  2009    4.673600\n",
       "6   Egypt, Arab Rep.  2008    7.156284\n",
       "7   Egypt, Arab Rep.  2007    7.087827\n",
       "8   Egypt, Arab Rep.  2006    6.843838\n",
       "9   Egypt, Arab Rep.  2005    4.471744\n",
       "10  Egypt, Arab Rep.  2004    4.092072"
      ]
     },
     "execution_count": 249,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "gdpgrowth_wb = wb.download(indicator='NY.GDP.MKTP.KD.ZG', country=['EG'], start=1991, end=2014)\n",
    "gdpgrowth_wb = gdpgrowth_wb.rename(columns = {'NY.GDP.MKTP.KD.ZG':'gdp_growth'})\n",
    "gdpgrowth_wb = gdpgrowth_wb.reset_index()\n",
    "gdpgrowth_wb.year = gdpgrowth_wb.year.astype(int)\n",
    "gdpgrowth_wb.head(-13)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Again, the growth is seen to be not as significant that last few years, after the crisis in 2009, however quite high increases up to 2009."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 250,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Implementing unemployment data from excel file"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 251,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "    year  unemployment\n",
      "0   1990         8.044\n",
      "1   1991         8.791\n",
      "2   1992         8.952\n",
      "3   1993        10.911\n",
      "4   1994        11.143\n",
      "5   1995        11.176\n",
      "6   1996         9.467\n",
      "7   1997         8.671\n",
      "8   1998         7.955\n",
      "9   1999         7.692\n",
      "10  2000         8.995\n",
      "11  2001         8.808\n",
      "12  2002        10.050\n",
      "13  2003        11.275\n",
      "14  2004        10.526\n",
      "15  2005        11.468\n",
      "16  2006        10.917\n",
      "17  2007         9.205\n",
      "18  2008         8.767\n",
      "19  2009         9.367\n",
      "20  2010         9.210\n",
      "21  2011        10.379\n",
      "22  2012        12.372\n",
      "23  2013        13.000\n",
      "24  2014        13.366\n"
     ]
    }
   ],
   "source": [
    "unempl = pd.read_excel('Egypt Unemployment.xlsx')\n",
    "print(unempl)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Its clear its quite a swinging unemployment rate, with no real pattern at the first glance. However, the rate is decreasing from 2005 to 2009, to then increase afterwards, in correlation to the financial crisis, which also is seems to be linked to the decrease in relative GDP growth those years. Furthermore, during the years with a high growth in GDP, from 2006 to 2008, the unemployment rate is at near lowest point for the period. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 252,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Changing type"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 253,
   "metadata": {},
   "outputs": [],
   "source": [
    "gdpgrowth_wb.year = gdpgrowth_wb.year.astype(int)\n",
    "gdp_wb.year = gdp_wb.year.astype(int)\n",
    "unempl.year = unempl.year.astype(int)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 254,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Merging data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 255,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(25, 2)\n",
      "(24, 3)\n",
      "(25, 4)\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>year</th>\n",
       "      <th>unemployment</th>\n",
       "      <th>country</th>\n",
       "      <th>gdp_growth</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>16</th>\n",
       "      <td>2006</td>\n",
       "      <td>10.917</td>\n",
       "      <td>Egypt, Arab Rep.</td>\n",
       "      <td>6.843838</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>1996</td>\n",
       "      <td>9.467</td>\n",
       "      <td>Egypt, Arab Rep.</td>\n",
       "      <td>4.988731</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>1998</td>\n",
       "      <td>7.955</td>\n",
       "      <td>Egypt, Arab Rep.</td>\n",
       "      <td>5.575497</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>14</th>\n",
       "      <td>2004</td>\n",
       "      <td>10.526</td>\n",
       "      <td>Egypt, Arab Rep.</td>\n",
       "      <td>4.092072</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>22</th>\n",
       "      <td>2012</td>\n",
       "      <td>12.372</td>\n",
       "      <td>Egypt, Arab Rep.</td>\n",
       "      <td>2.226200</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>15</th>\n",
       "      <td>2005</td>\n",
       "      <td>11.468</td>\n",
       "      <td>Egypt, Arab Rep.</td>\n",
       "      <td>4.471744</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    year  unemployment           country  gdp_growth\n",
       "16  2006        10.917  Egypt, Arab Rep.    6.843838\n",
       "6   1996         9.467  Egypt, Arab Rep.    4.988731\n",
       "8   1998         7.955  Egypt, Arab Rep.    5.575497\n",
       "14  2004        10.526  Egypt, Arab Rep.    4.092072\n",
       "22  2012        12.372  Egypt, Arab Rep.    2.226200\n",
       "15  2005        11.468  Egypt, Arab Rep.    4.471744"
      ]
     },
     "execution_count": 255,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "mergeddata = pd.merge(unempl, gdpgrowth_wb, how='outer', on = ['year'])\n",
    "print(unempl.shape)\n",
    "print(gdpgrowth_wb.shape)\n",
    "print(mergeddata.shape)\n",
    "mergeddata.sample(6)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 256,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Sorting data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 257,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>year</th>\n",
       "      <th>unemployment</th>\n",
       "      <th>country</th>\n",
       "      <th>gdp_growth</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1990</td>\n",
       "      <td>8.044</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1991</td>\n",
       "      <td>8.791</td>\n",
       "      <td>Egypt, Arab Rep.</td>\n",
       "      <td>1.125405</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1992</td>\n",
       "      <td>8.952</td>\n",
       "      <td>Egypt, Arab Rep.</td>\n",
       "      <td>4.472859</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1993</td>\n",
       "      <td>10.911</td>\n",
       "      <td>Egypt, Arab Rep.</td>\n",
       "      <td>2.900791</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1994</td>\n",
       "      <td>11.143</td>\n",
       "      <td>Egypt, Arab Rep.</td>\n",
       "      <td>3.973172</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>1995</td>\n",
       "      <td>11.176</td>\n",
       "      <td>Egypt, Arab Rep.</td>\n",
       "      <td>4.642459</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>1996</td>\n",
       "      <td>9.467</td>\n",
       "      <td>Egypt, Arab Rep.</td>\n",
       "      <td>4.988731</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>1997</td>\n",
       "      <td>8.671</td>\n",
       "      <td>Egypt, Arab Rep.</td>\n",
       "      <td>5.492355</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>1998</td>\n",
       "      <td>7.955</td>\n",
       "      <td>Egypt, Arab Rep.</td>\n",
       "      <td>5.575497</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>1999</td>\n",
       "      <td>7.692</td>\n",
       "      <td>Egypt, Arab Rep.</td>\n",
       "      <td>6.053439</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>2000</td>\n",
       "      <td>8.995</td>\n",
       "      <td>Egypt, Arab Rep.</td>\n",
       "      <td>6.370004</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11</th>\n",
       "      <td>2001</td>\n",
       "      <td>8.808</td>\n",
       "      <td>Egypt, Arab Rep.</td>\n",
       "      <td>3.535252</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12</th>\n",
       "      <td>2002</td>\n",
       "      <td>10.050</td>\n",
       "      <td>Egypt, Arab Rep.</td>\n",
       "      <td>2.390204</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>13</th>\n",
       "      <td>2003</td>\n",
       "      <td>11.275</td>\n",
       "      <td>Egypt, Arab Rep.</td>\n",
       "      <td>3.193455</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>14</th>\n",
       "      <td>2004</td>\n",
       "      <td>10.526</td>\n",
       "      <td>Egypt, Arab Rep.</td>\n",
       "      <td>4.092072</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>15</th>\n",
       "      <td>2005</td>\n",
       "      <td>11.468</td>\n",
       "      <td>Egypt, Arab Rep.</td>\n",
       "      <td>4.471744</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>16</th>\n",
       "      <td>2006</td>\n",
       "      <td>10.917</td>\n",
       "      <td>Egypt, Arab Rep.</td>\n",
       "      <td>6.843838</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>17</th>\n",
       "      <td>2007</td>\n",
       "      <td>9.205</td>\n",
       "      <td>Egypt, Arab Rep.</td>\n",
       "      <td>7.087827</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>18</th>\n",
       "      <td>2008</td>\n",
       "      <td>8.767</td>\n",
       "      <td>Egypt, Arab Rep.</td>\n",
       "      <td>7.156284</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>19</th>\n",
       "      <td>2009</td>\n",
       "      <td>9.367</td>\n",
       "      <td>Egypt, Arab Rep.</td>\n",
       "      <td>4.673600</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>20</th>\n",
       "      <td>2010</td>\n",
       "      <td>9.210</td>\n",
       "      <td>Egypt, Arab Rep.</td>\n",
       "      <td>5.147235</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>21</th>\n",
       "      <td>2011</td>\n",
       "      <td>10.379</td>\n",
       "      <td>Egypt, Arab Rep.</td>\n",
       "      <td>1.764572</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>22</th>\n",
       "      <td>2012</td>\n",
       "      <td>12.372</td>\n",
       "      <td>Egypt, Arab Rep.</td>\n",
       "      <td>2.226200</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>23</th>\n",
       "      <td>2013</td>\n",
       "      <td>13.000</td>\n",
       "      <td>Egypt, Arab Rep.</td>\n",
       "      <td>2.185466</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>24</th>\n",
       "      <td>2014</td>\n",
       "      <td>13.366</td>\n",
       "      <td>Egypt, Arab Rep.</td>\n",
       "      <td>2.915912</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    year  unemployment           country  gdp_growth\n",
       "0   1990         8.044               NaN         NaN\n",
       "1   1991         8.791  Egypt, Arab Rep.    1.125405\n",
       "2   1992         8.952  Egypt, Arab Rep.    4.472859\n",
       "3   1993        10.911  Egypt, Arab Rep.    2.900791\n",
       "4   1994        11.143  Egypt, Arab Rep.    3.973172\n",
       "5   1995        11.176  Egypt, Arab Rep.    4.642459\n",
       "6   1996         9.467  Egypt, Arab Rep.    4.988731\n",
       "7   1997         8.671  Egypt, Arab Rep.    5.492355\n",
       "8   1998         7.955  Egypt, Arab Rep.    5.575497\n",
       "9   1999         7.692  Egypt, Arab Rep.    6.053439\n",
       "10  2000         8.995  Egypt, Arab Rep.    6.370004\n",
       "11  2001         8.808  Egypt, Arab Rep.    3.535252\n",
       "12  2002        10.050  Egypt, Arab Rep.    2.390204\n",
       "13  2003        11.275  Egypt, Arab Rep.    3.193455\n",
       "14  2004        10.526  Egypt, Arab Rep.    4.092072\n",
       "15  2005        11.468  Egypt, Arab Rep.    4.471744\n",
       "16  2006        10.917  Egypt, Arab Rep.    6.843838\n",
       "17  2007         9.205  Egypt, Arab Rep.    7.087827\n",
       "18  2008         8.767  Egypt, Arab Rep.    7.156284\n",
       "19  2009         9.367  Egypt, Arab Rep.    4.673600\n",
       "20  2010         9.210  Egypt, Arab Rep.    5.147235\n",
       "21  2011        10.379  Egypt, Arab Rep.    1.764572\n",
       "22  2012        12.372  Egypt, Arab Rep.    2.226200\n",
       "23  2013        13.000  Egypt, Arab Rep.    2.185466\n",
       "24  2014        13.366  Egypt, Arab Rep.    2.915912"
      ]
     },
     "execution_count": 257,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "mergeddata.sort_index()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 258,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Cleaning data, and converting to a float (dropping by instances of missing data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 259,
   "metadata": {},
   "outputs": [],
   "source": [
    "mergeddata = mergeddata.dropna()\n",
    "mergeddata.unemployment = mergeddata.unemployment.astype('float')\n",
    "mergeddata.gdp_growth = mergeddata.gdp_growth.astype('float')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Part 2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 260,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Analyzing data with statistics"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 261,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "count    24.000000\n",
       "mean      4.303265\n",
       "std       1.733006\n",
       "min       1.125405\n",
       "25%       2.912132\n",
       "50%       4.472302\n",
       "75%       5.513140\n",
       "max       7.156284\n",
       "Name: gdp_growth, dtype: float64"
      ]
     },
     "execution_count": 261,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "mergeddata['gdp_growth'].describe()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The mean of the growth of GDP is 4.303, which does show quite a large positive growth in gdp during the period, while highest growth was a staggering 7.1562 percent, and lowest 1.1254 percent."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 262,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "count    24.000000\n",
       "mean     10.102625\n",
       "std       1.532183\n",
       "min       7.692000\n",
       "25%       8.916000\n",
       "50%       9.758500\n",
       "75%      11.151250\n",
       "max      13.366000\n",
       "Name: unemployment, dtype: float64"
      ]
     },
     "execution_count": 262,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "mergeddata['unemployment'].describe()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Here the first number that jumps to the eye, is the mean - the overall change for the periode, which is 10.102. This tells us, that the unemployment rate overall is increasing during the period. The highest rate recorded was 13.366 percent in 2014, which tells us Egypt is still trying to overcome the financial crisis. The lowest point recorded is 7.692 in 1999 , which is quite a large amount of the workforce in unemployment, however its almost half of the worst situation in 2014.\n",
    "In addition, a certain amount of dispersion in the data seems present, which the std (standard deviation) tells us."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 263,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Calculation of the correlation between the two"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 264,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>year</th>\n",
       "      <th>unemployment</th>\n",
       "      <th>gdp_growth</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>year</th>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.457167</td>\n",
       "      <td>-0.041357</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>unemployment</th>\n",
       "      <td>0.457167</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>-0.490076</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>gdp_growth</th>\n",
       "      <td>-0.041357</td>\n",
       "      <td>-0.490076</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                  year  unemployment  gdp_growth\n",
       "year          1.000000      0.457167   -0.041357\n",
       "unemployment  0.457167      1.000000   -0.490076\n",
       "gdp_growth   -0.041357     -0.490076    1.000000"
      ]
     },
     "execution_count": 264,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "mergeddata.corr(method='pearson')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The correlation between the unemployment and the growth is calcualted, to check whether or not Okun's law is fulfilled here.\n",
    "This calculation tells us, that to a growth in GDP by 1, a raise in unemployment on 0.457 percent follows, which is not at all in link to Okun's law. It does not make sense logically or for most of the data, however an explanation for this result could be that Egypt have been struggling the past decade."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 265,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Positive growth?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 266,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>year</th>\n",
       "      <th>unemployment</th>\n",
       "      <th>country</th>\n",
       "      <th>gdp_growth</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1991</td>\n",
       "      <td>8.791</td>\n",
       "      <td>Egypt, Arab Rep.</td>\n",
       "      <td>1.125405</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1992</td>\n",
       "      <td>8.952</td>\n",
       "      <td>Egypt, Arab Rep.</td>\n",
       "      <td>4.472859</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1993</td>\n",
       "      <td>10.911</td>\n",
       "      <td>Egypt, Arab Rep.</td>\n",
       "      <td>2.900791</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1994</td>\n",
       "      <td>11.143</td>\n",
       "      <td>Egypt, Arab Rep.</td>\n",
       "      <td>3.973172</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>1995</td>\n",
       "      <td>11.176</td>\n",
       "      <td>Egypt, Arab Rep.</td>\n",
       "      <td>4.642459</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   year  unemployment           country  gdp_growth\n",
       "1  1991         8.791  Egypt, Arab Rep.    1.125405\n",
       "2  1992         8.952  Egypt, Arab Rep.    4.472859\n",
       "3  1993        10.911  Egypt, Arab Rep.    2.900791\n",
       "4  1994        11.143  Egypt, Arab Rep.    3.973172\n",
       "5  1995        11.176  Egypt, Arab Rep.    4.642459"
      ]
     },
     "execution_count": 266,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "I = mergeddata['unemployment'] > 0\n",
    "mergeddata.loc[I, :].head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "In addition, a somewhat decent positive growth is shown here from 1991 to 1995, to an increase in unemployment. This is not in link with Okuns law either, and could also support the result we found, doing the correlation."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 267,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Plot 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 268,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "def plot(mergeddata):\n",
    "   mergeddata_indexed = mergeddata.set_index('year')\n",
    "   mergeddata_indexed.plot(legend=True)\n",
    "    \n",
    "plot(mergeddata)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "This plots enlightens us on the contradiction between the two, whereas the increase in unemployment is followed by an somewhat relative increase in GDP. Its quite clear from mid to late 90's, and from early 2000's to late 2000's, where an increase in both sections is seen. Its somewhat inconclusive during some of the periods, however the overall link is clear."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 269,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Plot 2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 270,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Text(0, 0.5, 'unemployment')"
      ]
     },
     "execution_count": 270,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "xy = mergeddata.plot(x = 'unemployment', y = 'gdp_growth', kind = 'scatter') \n",
    "xy.set_xlabel('gdp_growth') \n",
    "xy.set_ylabel('unemployment')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "This plot does also support the results we found prior to this section, it shows us that there is a positive correlation between GDP and unemployment, which completely contradicts Okun's law"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 271,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Additional packages"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 272,
   "metadata": {},
   "outputs": [],
   "source": [
    "from numpy import arange,array,ones\n",
    "from scipy import stats"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 273,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Using regression"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 274,
   "metadata": {},
   "outputs": [],
   "source": [
    "x = mergeddata['unemployment'] \n",
    "y = mergeddata['gdp_growth']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 275,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Clear overview"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 276,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Text(0.5, 0, 'unemployment')"
      ]
     },
     "execution_count": 276,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)\n",
    "line = slope*x+intercept\n",
    "\n",
    "plt.plot(x,y,'o', x, line)\n",
    "ax = plt.gca()\n",
    "fig = plt.gcf()\n",
    "ax.set_ylabel('gdp_growth') \n",
    "ax.set_xlabel('unemployment')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Here the linear fit based on the prior scatterplot furthermore underlines the positive, yet surprising correlation between GDP and unemployment, however a rather large portion of the datapoints does not seem to be near the regresion line at all."
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
