cd ..
if [ -e "server.jar" ]; then
    echo Server started
elif [ -e "../" ]; then
    echo Error: parent directory not found
else
    echo Error: file not found
fi