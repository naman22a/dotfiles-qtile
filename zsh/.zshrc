# My zsh stuff
if [[ -r "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh" ]]; then
  source "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh"
fi

export ZSH="$HOME/.oh-my-zsh"
ZSH_THEME="spaceship"
plugins=(git zsh-autosuggestions zsh-syntax-highlighting)

source $ZSH/oh-my-zsh.sh

# To customize prompt, run `p10k configure` or edit ~/.p10k.zsh.
[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh

# pfetch on startup
typeset -g POWERLEVEL9K_INSTANT_PROMPT=quiet
# colorscript -r


### EXPORTS

export TERM="xterm-256color"                  # getting proper colors
export PATH="$PATH:$HOME/.local/bin"
export PATH="$PATH:$HOME/.scripts"
# export NODE_OPTIONS=--openssl-legacy-provider
export LANG=en_US.UTF-8                       # fix font in tmux
export LC_CTYPE=en_US.UTF-8                   # fix font in tmux
export EDITOR="/usr/bin/lvim"                 # default terminal editor
export PATH="$PATH:$HOME/.emacs.d/bin"

# fnm
# export PATH=/home/naman/.fnm:$PATH
# eval "`fnm env`"
# eval "$(fnm env --use-on-cd)"

# nvm
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion

# yarn path
export PATH="$PATH:/opt/yarn-[version]/bin"
export PATH="$PATH:$HOME/.yarn/bin"

# llvm path (some stuff for c++)
# export PATH="$HOME/tools/llvm-project/build/bin:$PATH"
# export LD_LIBRARY_PATH="$HOME/tools/llvm-project/build/lib:$LD_LIBRARY_PATH"

# for golbally installed npm packages
export PATH="/home/naman/.nvm/versions/node/v17.4.0/bin:$PATH"

# for cargo
export PATH="/home/naman/.cargo/bin/:$PATH"

# for ruby
export PATH="/home/naman/.local/share/gem/ruby/3.0.0/bin:$PATH"

### ALIASES

# The command alias to start the browser-sync server
alias serve="browser-sync start --server --files . --no-notify --host $SERVER_IP --port 3000"

# the command alias to python3
alias py="python3"

# the command alias to lvim
alias nv="lvim"

# create react app
alias cra="yarn create react-app ./ --template typescript"

# create react app
alias cna="yarn create next-app ./ --ts"

# confirm before overwriting something
alias cp="cp -i"
alias mv='mv -i'
alias rm='rm -i'

alias mkdir="mkdir -pv"
alias hst="history 1 -1 | cut -c 8- | sort | uniq | fzf | tr -d '\n' | xclip -sel c"

# Colorize grep output (good for log files)
alias grep='grep --color=auto'
alias egrep='egrep --color=auto'
alias fgrep='fgrep --color=auto'

# cd
alias ..='cd ..'
alias ...='cd ...'

# lolcat
alias cat='lolcat'

alias lg='lazygit'

alias ls='lsd'
