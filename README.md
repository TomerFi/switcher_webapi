<h1>
  Switcher Web API
  <br/>
  <a href="https://hub.docker.com/r/tomerfi/switcher_webapi">
    <img src="https://img.shields.io/docker/v/tomerfi/switcher_webapi?color=%230A6799&logo=docker"/>
  </a>
  <a href="https://hub.docker.com/r/tomerfi/switcher_webapi">
    <img src="https://img.shields.io/docker/pulls/tomerfi/switcher_webapi.svg?logo=docker&label=pulls"/>
  </a>
  <a href="https://github.com/TomerFi/switcher_webapi/blob/dev/LICENSE">
    <img src="https://img.shields.io/github/license/tomerfi/switcher_webapi"/>
  </a>
  <br/>
  <a href="https://github.com/TomerFi/switcher_webapi/actions/workflows/stage.yml">
    <img src="https://github.com/TomerFi/switcher_webapi/actions/workflows/stage.yml/badge.svg"/>
  </a>
  <a href="https://github.com/TomerFi/switcher_webapi/actions/workflows/pages.yml">
    <img src="https://github.com/TomerFi/switcher_webapi/actions/workflows/pages.yml/badge.svg"/>
  </a>
  <a href="https://codecov.io/gh/TomerFi/switcher_webapi">
    <img src="https://codecov.io/gh/TomerFi/switcher_webapi/graph/badge.svg"/>
  </a>
</h1>

<strong>Gain containerized access to your local <a href="https://www.switcher.co.il/">Switcher</a> smart devices</strong>

```shell
docker run -d -p 8000:8000 --name switcher_webapi tomerfi/switcher_webapi:latest
```

<table align="left">
<tr>
  <td align="left">
    <a href="https://switcher-webapi.tomfi.info" target="_blank">Docs: https://switcher-webapi.tomfi.info</a>
  </td>
</tr>
</table>
<br/><br/><br/>

> [!IMPORTANT]  
> Since version 2.x.x, all endpoints require a device type. See [docs](https://switcher-webapi.tomfi.info/).
