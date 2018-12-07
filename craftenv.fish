set -x craftRoot (realpath (dirname (status filename)))

if command -v python3.7 >/dev/null
    set -x CRAFT_PYTHON_BIN (command -v python3.7)
else if command -v python3.6 >/dev/null
    set -x CRAFT_PYTHON_BIN (command -v python3.6)
else
    # could not find python 3.6, try python3
    if not command -v python3 >/dev/null
        echo "Failed to python Python 3.6+"
        exit 1
    end
    # check if python3 is at least version 3.6:
    set python_version (python3 --version)
    # sort and use . as separator and then check if the --version output is sorted later
    # Note: this is just a sanity check. craft.py should check sys.version
    set comparison (printf '%s\nPython 3.6.0\n' "$python_version" | sort -t.)
    if test (echo "$comparison" | head -n1) != "Python 3.6.0"
        echo "Found Python3 version $python_version is too old. Need at least 3.6"
        exit 1
    end
    set -x CRAFT_PYTHON_BIN (command -v python3)
end

set CRAFT_ENV (eval $CRAFT_PYTHON_BIN $craftRoot/bin/CraftSetupHelper.py --setup)
function export_lines
    for line in $argv
#        echo Line: $line
        set parts (string split '=' $line)
#        echo Set $parts[1] to $parts[2]
        set -gx $parts[1] $parts[2]
    end
end
export_lines $CRAFT_ENV

function craft
    eval $CRAFT_PYTHON_BIN $craftRoot/bin/craft.py $argv
end

function cs
    set dir (craft -q --ci-mode --get "sourceDir()" $argv)
    if test $status > 0
        echo $dir
    else
        cd $dir
    end
end

function cb
    echo $argv
    craft -q --ci-mode --get "buildDir()" $argv
    set dir (craft -q --ci-mode --get "buildDir()" $argv)
    if test $status > 0
        echo $dir
    else
        cd $dir
    end
end

function cr
    cd $KDEROOT
end

cr
