#!/bin/bash

if [ -z "$1" ]
then
  echo "You must pass in a topic name to delete."
else
  if [ -z "$2" ]
  then
    echo "No subscription name given. Subscription not removed."
  else
    echo Deleting pubsub subscription: $2 for topic: $1
    gcloud pubsub subscriptions delete $2 
    echo Fiished deleting pubsub subscription: $2 for topic: $1
  fi

  echo Deleting pubsub topic: $1
  gcloud pubsub topics delete $1
  echo Finished deleting pubsub topic: $1
fi
