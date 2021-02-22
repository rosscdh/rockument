FROM golang:alpine as builder

RUN apk --update add git build-base
RUN go get -u github.com/caddyserver/xcaddy/cmd/xcaddy
WORKDIR /src
COPY ./caddy-s3-proxy .
RUN cd caddy-s3-proxy;make build

FROM scratch

COPY --from=builder /src/caddy /caddy

ENTRYPOINT [ "./caddy" ]