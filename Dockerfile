FROM ubuntu:latest

ARG DEBIAN_FROTEND=nonninteractive

WORKDIR /workspace

CMD ["sleep", "infinity"]