{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "90f790b0",
   "metadata": {},
   "source": [
    "exerxice 01"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "20f1935d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "55 est la maximum\n"
     ]
    }
   ],
   "source": [
    "def maximum(a,b,c):\n",
    "    if(a>b and a>c):\n",
    "        print(a,\"est le maximum\")\n",
    "    if b>a and b>c:\n",
    "        print(b,\"est le maximum\")\n",
    "    if c>a and c>b:\n",
    "        print(c,\"est la maximum\")\n",
    "maximum(15,2,55)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2ae6e309",
   "metadata": {},
   "source": [
    "exercice 02"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "8213b479",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "entrez une lettreu\n",
      "u est voyelle.\n"
     ]
    }
   ],
   "source": [
    "def voyelle(lettre):\n",
    "    th=str(input(\"entrez une lettre\"))\n",
    "    if th=='a' or th=='e' or th=='i' or th=='o' or th=='u' or th=='y' :\n",
    "        print(th,\"est voyelle.\")\n",
    "    else :\n",
    "         print(th,\"est une consonne\")\n",
    "voyelle(\"e\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a2398fb5",
   "metadata": {},
   "source": [
    "exercice 03"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "id": "793ccfc1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "entrez le numero du jour2\n",
      "Mardi\n"
     ]
    }
   ],
   "source": [
    "def jour(nombre):\n",
    "    \n",
    "    a=int(input(\"entrez le numero du jour\"))\n",
    "    if(a == 1):\n",
    "        print(\"lundi\")\n",
    "    if(a == 2):\n",
    "        print(\"Mardi\")\n",
    "    if(a == 3):\n",
    "        print(\"Mercredi\")   \n",
    "    if(a == 4):\n",
    "        print(\"jeudi\")\n",
    "    if(a == 5):\n",
    "        print(\"vendredi\")\n",
    "    if(a == 6):\n",
    "        print(\"samedi\")\n",
    "    if(a == 7):\n",
    "        print(\"dimanche\")\n",
    "\n",
    "jour(4)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d5513b88",
   "metadata": {},
   "source": [
    "exercice 03"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 101,
   "id": "94c7fb10",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "c est une perte\n"
     ]
    }
   ],
   "source": [
    "def commerce(pv,pf):\n",
    "    if(pf<pv):\n",
    "        print(\"c est un profit\")\n",
    "    else:\n",
    "        print(\"c est une perte\")\n",
    "commerce(500,800)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4826355e",
   "metadata": {},
   "source": [
    "exercice 5"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 118,
   "id": "84679957",
   "metadata": {},
   "outputs": [],
   "source": [
    "def annee():\n",
    "    x=int(input(\"entrez le nombre jour de l'ans\"))\n",
    "    if x%4==0 and x%100!=0:\n",
    "        print(x,\"est une annee bisextille \")\n",
    "    else:\n",
    "        print(x,\"est une annee simple \")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 119,
   "id": "e3ece5a8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "entrez le nombre jour de l'ans365\n",
      "365 est une annee simple \n"
     ]
    }
   ],
   "source": [
    "annee()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "12e9ddee",
   "metadata": {},
   "source": [
    "exercice 06"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 96,
   "id": "8d5367dc",
   "metadata": {},
   "outputs": [],
   "source": [
    "def etoile (carbo):\n",
    "    for i in range(1,carbo+1):\n",
    "        print(i*\"*\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 97,
   "id": "9184194e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "*\n",
      "**\n",
      "***\n",
      "****\n",
      "*****\n"
     ]
    }
   ],
   "source": [
    "etoile(5)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "80daf3e3",
   "metadata": {},
   "source": [
    "exercice 7"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "27566123",
   "metadata": {},
   "outputs": [],
   "source": [
    "def infos():\n",
    "    x=input(\"testez avec le informatique\")\n",
    "    nvoy=0\n",
    "    p=len(x)\n",
    "    for i in range(0,p):\n",
    "        if x [i] in ['a','o','u','i','y','e']:\n",
    "            nvoy=nvoy+1\n",
    "    print(\"le  mot possede \",nvoy,\"  voyelles\")\n",
    "      "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "862ed30e",
   "metadata": {},
   "source": [
    "infos()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "796a1613",
   "metadata": {},
   "source": [
    "exercice 08"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 83,
   "id": "06ce059d",
   "metadata": {},
   "outputs": [],
   "source": [
    "def nombre(a):\n",
    "    for i in range(0,18,3):\n",
    "        print(i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 110,
   "id": "942f4404",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0\n",
      "3\n",
      "6\n",
      "9\n",
      "12\n",
      "15\n"
     ]
    }
   ],
   "source": [
    "nombre(18)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "724af027",
   "metadata": {},
   "source": [
    "exercice 9"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b0afc1a0",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "999b63c9",
   "metadata": {},
   "outputs": [],
   "source": [
    "       "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1eafd631",
   "metadata": {},
   "source": [
    "exercice 10"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "fb221483",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Vous devez répondre par 'oui' ou bien 'non'\n",
      "vous etes adulte non\n"
     ]
    }
   ],
   "source": [
    "def reponse(rep):\n",
    "    #(\"Il faut répondre par oui ou non\\n\")\n",
    "    if rep!=\"oui\" and rep!=\"non\":\n",
    "        print(\"Vous devez répondre par 'oui' ou bien 'non'\")\n",
    "        rep=input(\"vous etes adulte \")\n",
    "    else:\n",
    "        print(\"Au revoir\")\n",
    "reponse(\"rep\") \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "551b7e82",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "0929d5ee",
   "metadata": {},
   "source": [
    "exercice 11"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 192,
   "id": "1fe8a796",
   "metadata": {},
   "outputs": [],
   "source": [
    "def alleatoire():\n",
    "    import random\n",
    "    x=random.randint(1,100)\n",
    "    y=17\n",
    "    while (x >0):\n",
    "        x-=1\n",
    "        var=int(input(\"devinez un nombre \"))\n",
    "        if var< x:\n",
    "            print(\"plus petit\")\n",
    "        elif(var >x):\n",
    "            print(\"plus grand\")\n",
    "        else:\n",
    "            print(\"vous avez trouvé\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5c5a49da",
   "metadata": {},
   "outputs": [],
   "source": [
    "alleatoire()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ae60a87a",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "13e56013",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d81a065e",
   "metadata": {},
   "outputs": [],
   "source": [
    "exo12"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 201,
   "id": "65cde7ce",
   "metadata": {},
   "outputs": [],
   "source": [
    "def pgdc():\n",
    "    a=int(input(\"entrezun nombre\"))\n",
    "    b=int(input(\"entrez un nombre\"))\n",
    "    if a>b:\n",
    "        max=b\n",
    "    else:\n",
    "        max=a\n",
    "    for i in range(1,min+1):\n",
    "        if a%i==0 and b%i==0:\n",
    "                    pgdc=1\n",
    "                    print(\"le pgdc est \",pgdc)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "38ed1583",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "269df2e4",
   "metadata": {},
   "source": [
    "exercice 13"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 203,
   "id": "9af42e1c",
   "metadata": {},
   "outputs": [],
   "source": [
    "def nombre():\n",
    "    for i in range (1,6):\n",
    "        for i in range (10):\n",
    "            print(i,end=\"  \")\n",
    "        print(\"\\n\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 123,
   "id": "d04dd178",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0  1  2  3  4  5  6  7  8  9  \n",
      "\n",
      "0  1  2  3  4  5  6  7  8  9  \n",
      "\n",
      "0  1  2  3  4  5  6  7  8  9  \n",
      "\n",
      "0  1  2  3  4  5  6  7  8  9  \n",
      "\n",
      "0  1  2  3  4  5  6  7  8  9  \n",
      "\n"
     ]
    }
   ],
   "source": [
    "nombre()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7a35c21e",
   "metadata": {},
   "source": [
    "exercice 14"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b29f206b",
   "metadata": {},
   "outputs": [],
   "source": [
    "def somme():\n",
    "    som=0\n",
    "    for i in range(1,4):\n",
    "        n=int(input(\"entrez un nombre \"))\n",
    "        som=som+i\n",
    "        print(i)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a213b724",
   "metadata": {},
   "source": [
    "exercice 15"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "08f5e08b",
   "metadata": {},
   "outputs": [],
   "source": [
    "def carre() :   \n",
    "        som=0\n",
    "        for i in range(1,10):\n",
    "            ca=i *i\n",
    "            som= som+ ca\n",
    "            print(i,\"son carré est\",ca)\n",
    "        print(som,\"la somme des carres des nombres compris entre 1 et 10\")\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "fd7c602a",
   "metadata": {},
   "source": [
    "exercice 16"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 124,
   "id": "52ee9a46",
   "metadata": {},
   "outputs": [],
   "source": [
    "def divisible():\n",
    "    for i in range(7,150):\n",
    "        if(i % 7 ==0):\n",
    "            print(i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 125,
   "id": "b4342490",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "7\n",
      "14\n",
      "21\n",
      "28\n",
      "35\n",
      "42\n",
      "49\n",
      "56\n",
      "63\n",
      "70\n",
      "77\n",
      "84\n",
      "91\n",
      "98\n",
      "105\n",
      "112\n",
      "119\n",
      "126\n",
      "133\n",
      "140\n",
      "147\n"
     ]
    }
   ],
   "source": [
    "divisible()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "09d63eee",
   "metadata": {},
   "source": [
    "exercice 17"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "aaac1d2d",
   "metadata": {},
   "outputs": [],
   "source": [
    "def racine():\n",
    "    i=1\n",
    "    while i*i <= 1000:\n",
    "        i =i+1\n",
    "\n",
    "    print(i)  "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2393d451",
   "metadata": {},
   "source": [
    "exercice 18"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 126,
   "id": "d35d7099",
   "metadata": {},
   "outputs": [],
   "source": [
    "def armstrong():\n",
    "    nb=int(input(\"entrez un nombre \"))\n",
    "    s=0\n",
    "    tmp=nb\n",
    "    while tmp>0:\n",
    "        d=tmp % 10\n",
    "        s+=d**3\n",
    "        tmp//=10\n",
    "    if nb==s:\n",
    "        print(nb,\"est un nombre armstrong\")\n",
    "    else:\n",
    "        print(nb,\"n est pas  un nombre armstrong \")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 127,
   "id": "5d65f9ea",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "entrez un nombre 153\n",
      "153 est un nombre armstrong\n"
     ]
    }
   ],
   "source": [
    "armstrong()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f21996d3",
   "metadata": {},
   "source": [
    "exercice 19"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 129,
   "id": "925ccdc1",
   "metadata": {},
   "outputs": [],
   "source": [
    "def parfait():\n",
    "    a=int(input('entrez un nombre !'))\n",
    "    sda=0\n",
    "    for i in range(1,a):\n",
    "        if(a%i==0):\n",
    "            sda=sda+i\n",
    "            i=i+1\n",
    "    if(sda == a):\n",
    "        print(a,'est un nombre parfait')\n",
    "    else:\n",
    "        print(a,'n est pas un nombre parfait')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 155,
   "id": "4072bf0d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "entrez un nombre !6\n",
      "6 est un nombre parfait\n"
     ]
    }
   ],
   "source": [
    "parfait()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9c04d620",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "23ead676",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "b4c0ef54",
   "metadata": {},
   "source": [
    "exercice 15"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "3d35bf97",
   "metadata": {},
   "outputs": [],
   "source": [
    "def carre() :   \n",
    "        som=0\n",
    "        for i in range(1,10):\n",
    "            ca=i *i\n",
    "            som= som+ ca\n",
    "            print(i,\"son carré est\",ca)\n",
    "        print(som,\"la somme des carres des nombres compris entre 1 et 10\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "186bfb10",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1 son carré est 1\n",
      "2 son carré est 4\n",
      "3 son carré est 9\n",
      "4 son carré est 16\n",
      "5 son carré est 25\n",
      "6 son carré est 36\n",
      "7 son carré est 49\n",
      "8 son carré est 64\n",
      "9 son carré est 81\n",
      "285 la somme des carres des nombres compris entre 1 et 10\n"
     ]
    }
   ],
   "source": [
    "carre()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c99eb2a9",
   "metadata": {},
   "source": [
    "exercice 16"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "8f3e706b",
   "metadata": {},
   "outputs": [],
   "source": [
    "def divisible():\n",
    "    for i in range(7,150):\n",
    "        if(i % 7 ==0):\n",
    "            print(i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "d3e13346",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "7\n",
      "14\n",
      "21\n",
      "28\n",
      "35\n",
      "42\n",
      "49\n",
      "56\n",
      "63\n",
      "70\n",
      "77\n",
      "84\n",
      "91\n",
      "98\n",
      "105\n",
      "112\n",
      "119\n",
      "126\n",
      "133\n",
      "140\n",
      "147\n"
     ]
    }
   ],
   "source": [
    "divisible()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b6b99f33",
   "metadata": {},
   "source": [
    "exercice 17"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "4a21386b",
   "metadata": {},
   "outputs": [],
   "source": [
    "def racine():\n",
    "    i=1\n",
    "    while i*i <= 1000:\n",
    "        i =i+1\n",
    "\n",
    "    print(i)  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "8a1c26f9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "32\n"
     ]
    }
   ],
   "source": [
    "racine()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "19a568c9",
   "metadata": {},
   "source": [
    "exercice 19"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "id": "c6f8ac43",
   "metadata": {},
   "outputs": [],
   "source": [
    "def parfait():\n",
    "    a=int(input('entrez un nombre !'))\n",
    "    sda=0\n",
    "    for i in range(1,a):\n",
    "        if(a%i==0):\n",
    "            sda=sda+i\n",
    "            i=i+1\n",
    "    if(sda == a):\n",
    "        print(a,'est un nombre parfait')\n",
    "    else:\n",
    "        print(a,'n est pas un nombre parfait')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "id": "5ab71ebc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "entrez un nombre !6\n",
      "6 est un nombre parfait\n"
     ]
    }
   ],
   "source": [
    "parfait()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1395a8db",
   "metadata": {},
   "source": [
    "exercice 18"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "id": "6e527ff9",
   "metadata": {},
   "outputs": [],
   "source": [
    "def armstrong():\n",
    "    nb=int(input(\"entrez un nombre \"))\n",
    "    s=0\n",
    "    tmp=nb\n",
    "    while tmp>0:\n",
    "        d=tmp % 10\n",
    "        s+=d**3\n",
    "        tmp//=10\n",
    "    if nb==s:\n",
    "        print(nb,\"est un nombre armstrong\")\n",
    "    else:\n",
    "        print(nb,\"n est pas  un nombre armstrong \")\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 86,
   "id": "4061b54a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "entrez un nombre 450\n",
      "450 n est pas  un nombre armstrong \n"
     ]
    }
   ],
   "source": [
    "armstrong()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f40f4959",
   "metadata": {},
   "source": [
    "exercice 20"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 153,
   "id": "86c72046",
   "metadata": {},
   "outputs": [],
   "source": [
    "def ppmc():\n",
    "    c=int(input(\"entrez un nombre\"))\n",
    "    d=int(input(\"entrez un nombre\"))\n",
    "    multi=1\n",
    "    ppmc=0\n",
    "    if c>d:\n",
    "        ppmc=d\n",
    "    else:\n",
    "        ppmc=c\n",
    "    multi=c*d\n",
    "    while i> ppmc:\n",
    "        if i%c==0 and i%d==0:\n",
    "            multi*=1\n",
    "            print(\"le ppmc de \", c,\" et \",d,\" est :\",multi)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 154,
   "id": "846c4175",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "entrez un nombre141\n",
      "entrez un nombre255\n"
     ]
    }
   ],
   "source": [
    "ppmc()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "837f7285",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "\n",
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0533006d",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "24f5f29b",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e114ef24",
   "metadata": {},
   "outputs": [],
   "source": []
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
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
