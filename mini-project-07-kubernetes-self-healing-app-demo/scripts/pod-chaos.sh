#!/bin/bash

NAMESPACE="self-healing-demo"
APP_LABEL="app=self-healing-web"

echo "======================================"
echo " Kubernetes Self-Healing Demo"
echo "======================================"

echo ""
echo "Current pods before deletion:"
kubectl get pods -n $NAMESPACE -l $APP_LABEL -o wide

echo ""
echo "Selecting a random pod to delete..."

POD_NAME=$(kubectl get pods -n $NAMESPACE -l $APP_LABEL -o jsonpath='{.items[*].metadata.name}' | tr ' ' '\n' | shuf -n 1)

echo ""
echo "Deleting pod: $POD_NAME"
kubectl delete pod $POD_NAME -n $NAMESPACE

echo ""
echo "Pods immediately after deletion:"
kubectl get pods -n $NAMESPACE -l $APP_LABEL -o wide

echo ""
echo "Watching Kubernetes self-heal..."
echo "Press Ctrl+C after all pods are Running again."
kubectl get pods -n $NAMESPACE -l $APP_LABEL -w
