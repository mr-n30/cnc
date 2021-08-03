# cnc
Command aNd Control multiple servers from [DigitalOcean](https://www.digitalocean.com/)

# Installation
```bash
# pip install -r requirements.txt
```

# Setup
Example config.yaml:
```yaml
digitalocean:
    - <YOUR_API_KEY>
```

The following configures and creates your droplets
```bash
$ python3 cnc.py config -c config.yaml
```

Then run the following to configure your `/etc/hosts`:
```bash
# python3 cnc.py etc -c config.yaml
```
