import itertools
import random
import os

# ANSI colors
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
BLUE = "\033[94m"
RESET = "\033[0m"


def clear_screen():
    os.system("clear" if os.name == "posix" else "cls")

def logo():
    print(f"""{BLUE}
                                  X0OkkkkkO0KN
                             ko:'.    .....    ..;l
                         k:.   .:ok0NWMWWWWMNKkdc'   .;d
                      d,    .okkOOOOxdollloodkOOOkkx,    .o
                   O;     .xkoxOdllllllllllllllldkkoxO'     ,x
                 k.      ,Xcdkollllllllllllllllllllxx;Xc  .   .d
               K,       .N:.dllclllllllllllllllllcclo;.N, ;     .O
              o    'Nc  l0  cll,;lllllllllllllll:.lll. dk         :N
            N,          Oo  ,loo,lloolllllllooll;col:  ;N    :d.   .K
           X.           X;  .O0d;:llll:lll:llllc;l00,  .M.   ';     .0
          N'     lo    .M..c:c,'. ..,,.,;;.','. .',:c;. X:   .;      .X
          :      ,;  .lk0 lx'..  ..    ;;;.   ... ..'lk dOo.  .       'W
         O          .Kl;,.00x:,;ll:,,,;oll;;,,;cl:,:d0N'.c;X'    ,;    d
        M;  .lo;    cX  .OWNkooollc.;lclllccc.;lloolxXWN.. Ox    ld.   .M
        N   kMMM'   oK...dc;cccl:.';.  ...  .;'.;:ccc,co, .x0           0
        O   .cl,    :N.' ''. ...'cllll:. .;lllll,.....'' ..0x   ,;.     d
        k            xk. .;.    ....''''.'''''...    .'. .d0.  dMMX     o
        O            :Xc  ;c.l' .dK0OOkkkkkkO0Kk' .c';c  ;Xl.  .:c.     d
        N     '0:  .Kx.   .l:l;l:;cdkO0KKKK0kxl;;c;c:l;    oX;          0
        M,     .   Koo,   .lll'lc,dkddddlddddxxc;l'cll;   .k;N.        .W
         k   '.  .lX xx   :lll.lc.ll'lll.lll'cl;;l':llc.  lK Ox.  :.   o
         M;  .:dxd:. ;N, .cll;,l;'ll.lll.cll.:l;'l:'llc' .Xl .:oxxc.  .W
          X..o;,lxK, .oK. .cc.ll.cl:.lll.:ll,,ll':l':l,  0x' .Kxl;;o..K
           K. lxolx   :o.  ..'l.;ll.:lll :lll.llc.c;..  .dc.  dloxd. O
            X. ,l;'   ;c.     . ;::.lllc ;lll.,:;...    .c:   ';c: .0
             N:       ,c.       ... ',,' .,,,....       .c;       ,X
              O.     ,c;.           ...  ..            ,c:     .x
                 d.   .:lxo:.                       .;oxo:'   .o
                   x,   .,:lddl;.                ,cdxlc;.   .d
                      o'   .';cld'             .xoc:'.   .l
                         x:.   ...             .'..  .,
                             kl;'.              .,c

{CYAN}        Created by Alok Thakur - YouTube: Firewall Breaker {RESET}
""")

def get_cleaned_list(string):
    return [s.strip() for s in string.split(",") if s.strip()]

def generate_combinations(base_words, symbols, min_words=2000):
    print(f"\n{YELLOW}[+] Generating combinations... Please wait...{RESET}")
    all_passwords = set()

    for i in range(1, 4):
        for combo in itertools.permutations(base_words, i):
            joined = "".join(combo)
            for sym in symbols:
                p1 = joined + sym
                p2 = sym + joined
                if len(p1) <= 10:
                    all_passwords.add(p1)
                if len(p2) <= 10:
                    all_passwords.add(p2)
                if len(all_passwords) >= min_words:
                    return list(all_passwords)

    # Extend using modified variations if still not enough
    extra_words = list(all_passwords)
    tries = 0
    while len(all_passwords) < min_words and tries < 10000:
        word = random.choice(extra_words)
        for w in [word.lower(), word.upper(), word.capitalize()]:
            if len(w) <= 10:
                all_passwords.add(w)
        tries += 1

    return list(all_passwords)

def colorful_input(prompt):
    return input(f"\n{CYAN}{prompt}{RESET}")

def main():
    clear_screen()
    logo()
    print(f"{CYAN}          🔐 UltraPassGen - Advanced Wordlist Generator 🔐{RESET}\n")

    # User info
    fname = colorful_input("Enter your First Name: ")
    lname = colorful_input("Enter your Last Name: ")
    nick = colorful_input("Enter your Nickname: ")
    dob = colorful_input("Enter your Date of Birth (DDMMYYYY): ")
    phone = colorful_input("Enter your Phone Number: ")

    # Friend info
    f_fname = colorful_input("Enter Friend's First Name: ")
    f_lname = colorful_input("Enter Friend's Last Name: ")
    f_dob = colorful_input("Enter Friend's DOB (DDMMYYYY): ")

    # Girlfriend info
    g_fname = colorful_input("Enter Girlfriend's First Name: ")
    g_lname = colorful_input("Enter Girlfriend's Last Name: ")
    g_nick = colorful_input("Enter Girlfriend's Nickname: ")
    g_dob = colorful_input("Enter Girlfriend's DOB (DDMMYYYY): ")

    # Custom inputs
    custom = colorful_input("Enter custom words (comma-separated): ")
    symbols_input = colorful_input("Enter symbols (comma-separated, e.g. @,#,123): ")
    filename = colorful_input("Enter filename to save (e.g., wordlist.txt): ")

    words = [
        fname, lname, nick, dob, phone,
        f_fname, f_lname, f_dob,
        g_fname, g_lname, g_nick, g_dob
    ] + get_cleaned_list(custom)

    symbols = get_cleaned_list(symbols_input)
    words = list(set([w for w in words if w]))

    print(f"\n{YELLOW}[*] Total base words collected: {len(words)}{RESET}")
    passwords = generate_combinations(words, symbols)

    with open(filename, 'w') as file:
        for p in passwords:
            file.write(p + "\n")

    print(f"\n{GREEN}✅ Wordlist generated with {len(passwords)} passwords and saved as {filename}.{RESET}")

if __name__ == "__main__":
    main()
