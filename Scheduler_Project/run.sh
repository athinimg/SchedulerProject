#CUSTOMISE HERE
# =====================================================================
#Enter your student number here
student_num=studentnum
#Choose a data file between {easy, medium, hard, extreme}
data_file="easy" 
# =====================================================================




# DO NOT MODIFY BELOW THIS LINE
# ================================================================================================
marker_args="--data-file Data/$data_file.txt --student-num $student_num"
student_args="--data-file Data/$data_file.txt"

if command -v python3 &>/dev/null; then
    PYTHON_CMD=python3
    PYTHON_VERSION=$($PYTHON_CMD --version 2>&1 | awk '{print $2}')

    if [[ "$PYTHON_VERSION" != 3.11.* ]]; then
        echo "Error: Python version must be 3.11.*. Found: $PYTHON_VERSION"
        exit 1
    fi
else
    echo "Error: python3 is not installed."
    exit 1
fi

result=$($PYTHON_CMD $student_num.py $student_args | $PYTHON_CMD marker.pyc $marker_args)

echo "$result"
# ================================================================================================