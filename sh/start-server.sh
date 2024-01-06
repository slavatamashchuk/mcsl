cd ..
if [ -e "server.jar" ] && [ -e "eula.txt" ] && [ -e "server.properties" ]; then
    echo Server started
else
    echo Error: files not found
fi