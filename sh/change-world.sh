cd ..
if [ -e "world-survival" ] && [ -e "world" ]; then
    mv world-survival world_
    mv world world-creative
    mv world_ world
    echo Survival seted
elif [ -e "world-creative" ] && [ -e "world" ]; then
    mv world-creative world_
    mv world world-survival
    mv world_ world
    echo Creative seted
else
    echo Error: files not found
fi