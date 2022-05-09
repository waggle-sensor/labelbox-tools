# Labelbox Scripts

This repo contains a few exampels

## Generating a Labelbox API Key

In order to use most of these scripts, you'll need a Labelbox API Key. To do this:

1. Login to Labelbox.
2. Go to Account settings. (Click your account icon and then Account.)
3. Go to API tab.
4. Create API key. (You want to copy this, as it will only show up once. You can always generate a new one, of course.)

I'd recommend adding this to a _private_ `labelbox.env` file like:

```txt
export LABELBOX_API_KEY=...api key you just copied...
```

That way, you can easily prepare your environment using:

```sh
. labelbox.env
```
