# utils/truth_dare_engine.py
import random
import time
import os
import json
from utils.printer import print_delay

HISTORY_FILE = "data/truth_dare_history.json"

TRUTHS = {
    "😇": [
        "What's your go-to move to impress a crush in a terminal session?",
        "What's the sweetest thing you've ever typed into someone’s DMs?",
        "Ever fallen for someone during a hackathon? Who was it?",
        "Have you ever coded something romantic for someone?",
        "What’s your ideal “pair programming” date?"
    ],
    "😈": [
        "Describe the last dream you had… and don’t leave out the spicy parts.",
        "What’s the riskiest text you’ve ever sent?",
        "What command would you type to reboot your love life?",
        "What’s your biggest romantic “bug” you still haven’t fixed?",
        "What's something that turns you on… that shouldn't?"
    ],
    "🤯": [
        "If you were a kink-themed Linux distro, what would it be called and what would it do?",
        "What’s your “forbidden bash history” entry?",
        "Describe a romantic fantasy involving sudo privileges.",
        "Which package manager do you think is secretly the best kisser?",
        "What would your man page say under “Usage Examples” (spicy ones only)?"
    ]
}

DARES = {
    "😇": [
        "Type a love letter using cowsay and send it to someone you admire.",
        "Compliment someone’s GitHub profile like it’s a dating profile.",
        "Send a 🐧 emoji to the 3rd person on your contact list and say thinking of you.",
        "Use text-to-speech to confess your love to your favorite Linux command.",
        "Call someone and tell them you think they're as elegant as a Bash one-liner."
    ],
    "😈": [
        "Whisper “systemctl start feelings.service” in the sexiest voice possible.",
        "Write a shell script to flirt — then run it and read the output aloud.",
        "Post “looking for someone to mount my heart” in a public Discord/server.",
        "Use sed to turn an innocent message into something extremely flirty.",
        "Wear your headphones and moan the word “grep” like it’s your safe word."
    ],
    "🤯": [
        "Roleplay a seduction scene between Emacs and Vim (dramatized).",
        "Confess a fictional kink involving Linux distros and explain why.",
        "Rename your home folder to /dev/pleasure and explain it during your demo.",
        "Simulate “dirty talk” between two running processes.",
        "Say “I love your output stream” 5 different seductive ways."
    ]
}

ASCII_BANNER = r"""
 ********** *******   **     ** ********** **      **           **     ****     ** *******         *******       **     *******   ********
/////**/// /**////** /**    /**/////**/// /**     /**          ****   /**/**   /**/**////**       /**////**     ****   /**////** /**///// 
    /**    /**   /** /**    /**    /**    /**     /**         **//**  /**//**  /**/**    /**      /**    /**   **//**  /**   /** /**      
    /**    /*******  /**    /**    /**    /**********        **  //** /** //** /**/**    /**      /**    /**  **  //** /*******  /******* 
    /**    /**///**  /**    /**    /**    /**//////**       **********/**  //**/**/**    /**      /**    /** **********/**///**  /**////  
    /**    /**  //** /**    /**    /**    /**     /**      /**//////**/**   //****/**    **       /**    ** /**//////**/**  //** /**      
    /**    /**   //**//*******     /**    /**     /**      /**     /**/**    //***/*******        /*******  /**     /**/**   //**/********
    //     //     //  ///////      //     //      //       //      // //      /// ///////         ///////   //      // //     // //////// 
                                                                                                                                          
                                                                                                                                          
                                                                                                                                          
                                                                                                                                          
                                                                                                                                          
                                                                                                                                          
                                                                                                                                          
                                                                                                                                          """

def load_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE) as f:
            return json.load(f)
    return {"truths": [], "dares": []}

def save_to_history(type_, value):
    history = load_history()
    history[type_].append(value)
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=2)

def truth_or_dare():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(ASCII_BANNER)
    print_delay("Welcome to apt-love: TRUTH.exe or DARE.sh 🖥️💘\n", 0.03)

    while True:
        print("Choose your spice level:")
        print("  [1] 😇 Vanilla")
        print("  [2] 😈 Spicy")
        print("  [3] 🤯 WTF mode")
        print("  [4] Exit")
        spice = input("➤ ").strip()
        if spice == "4":
            print_delay("💔 Exiting Truth or Dare. Your secrets are safe... for now.")
            break

        if spice not in ["1", "2", "3"]:
            print_delay("⚠️ Invalid spice level. Try again.")
            continue

        spice_emoji = {"1": "😇", "2": "😈", "3": "🤯"}[spice]

        print("\nChoose your fate:")
        print("  [1] Truth")
        print("  [2] Dare")
        print("  [3] Back to spice level")
        choice = input("➤ ").strip()

        if choice == "1":
            print_delay("\n🧠 Fetching a spicy truth from the love archives...", 0.04)
            time.sleep(1)
            truth = random.choice(TRUTHS[spice_emoji])
            print("\n" + truth)
            save_to_history("truths", truth)
        elif choice == "2":
            print_delay("\n🚀 Deploying a wild dare to your emotional kernel...", 0.04)
            time.sleep(1)
            dare = random.choice(DARES[spice_emoji])
            print("\n" + dare)
            save_to_history("dares", dare)
        elif choice == "3":
            continue
        else:
            print_delay("⚠️ Invalid input. Maybe that was your dare?")
            continue

        print("\nPress Enter to continue...")
        input()
        os.system('cls' if os.name == 'nt' else 'clear')
        print(ASCII_BANNER)
