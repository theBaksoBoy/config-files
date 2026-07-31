# Enable Powerlevel10k instant prompt. Should stay close to the top of ~/.zshrc.
# Initialization code that may require console input (password prompts, [y/n]
# confirmations, etc.) must go above this block; everything else may go below.
if [[ -r "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh" ]]; then
  source "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh"
fi



# -------------------------------------------------- loading stuff



# using zinit for easy plugin management and reproducability when moving config to different systems
# set the directory to store zinit and plugins
ZINIT_HOME="${XDG_DATA_HOME:-${HOME}/.local/share}/zinit/zinit.git"
# if zinit is not installed then download it
if [ ! -d "$ZINIT_HOME" ]; then
    mkdir -p "$(dirname $ZINIT_HOME)"
    git clone https://github.com/zdharma-continuum/zinit.git "$ZINIT_HOME"
fi
source "${ZINIT_HOME}/zinit.zsh"

# add powerlevel10k
zinit ice depth=1; zinit light romkatv/powerlevel10k
# To customize prompt, run `p10k configure` or edit ~/.p10k.zsh.
[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh

# add plugins
zinit light zsh-users/zsh-syntax-highlighting
zinit light zsh-users/zsh-completions
zinit light zsh-users/zsh-autosuggestions
zinit light Aloxaf/fzf-tab

# load completions
# a plugin that gives you info of all your options and what they do when pressing tab after writing for instance "git "
autoload -U compinit && compinit

eval "$(fzf --zsh)"



# -------------------------------------------------- other configuration



export EDITOR=vim
export VISUAL=vim

bindkey -e

# history configuration
HISTSIZE=5000
SAVEHIST=$HISTSIZE
HISTFILE=~/.zsh_history
HISTDUP=erase
setopt appendhistory
setopt sharehistory
setopt hist_ignore_space
setopt hist_ignore_all_dups
setopt hist_save_no_dups
setopt hist_ignore_dups
setopt hist_find_no_dups

# completion styling
zstyle ':completion:*' matcher-list '' 'm:{a-z}={A-Z}' 'm:{a-zA-Z}={A-Za-z}' 'r:|[._-]=* r:|=* l:|=*'
zstyle ':completion:*' list-colors ${(s.:.)LS_COLORS}
zstyle ':completion:*' menu no
zstyle ':fzf-tab:complete:cd:*' fzf-preview 'ls --color $realpath'

# keybinds
# set keybinds for ctrl + arrows
bindkey "^[[1;5C" forward-word
bindkey "^[[1;5D" backward-word


# custom aliases
alias ls="ls --color"
alias emilate='"/home/bakso/programming/memory media tool/MemoryMediaTool.py"'
alias restartsoundserver='systemctl --user restart wireplumber pipewire pipewire-pulse'
alias turboupgrade='sudo apt update && sudo apt upgrade && flatpak update'
alias doomemacs="emacsclient -c -a 'emacs'"
alias pm="python3 main.py"
alias initializetablet='xinput set-prop 18 "Coordinate Transformation Matrix" -0.5 0 1 0 -1 1 0 0 1'
alias chunkvideo="/home/bakso/video_chunker.sh"
alias vpnon="nmcli connection up integrity2-SE"
alias vpnoff="nmcli connection down integrity2-SE"
alias tor="cd /home/bakso/Programs/tor-browser && ./start-tor-browser.desktop &"
alias moneylogger="./programming/money_logger/money_logger"

spk() {
	espeak -s 275 "$1"
}

codecify() {
	ffmpeg -i "$1" -c:v libx264 -crf 18 -preset fast -c:a copy "$2"
}

gitaddcommitpush() {
	echo -n "are you sure that you want to run this command (y/N) "
	read confirm
	if [[ $confirm == [yY] ]]; then
		git add . && git commit -m $1 && git push
	else
		echo "aborted"
	fi
}


# path exports
export PATH="$HOME/.config/emacs/bin:$PATH"
export PATH="$HOME/.local/bin:$PATH"
export PATH="$HOME/.local/odin:$PATH"








