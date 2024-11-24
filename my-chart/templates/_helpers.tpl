

{{/* Define a helper to generate the full MySQL connection URL */}}
{{- define "my-dvir-app.fullMySQLConnectionURL" -}}
jdbc:mysql://{{ .Release.Name }}-mysql-service:3306/{{ .Values.mysql.databaseName }}?createDatabaseIfNotExist=true&characterEncoding=UTF-8&useUnicode=true&useSSL=false&allowPublicKeyRetrieval=true
{{- end -}}

{{- define "imagePullSecret" }}
{{- with .Values.imageCredentials }}
{{- printf "{\"auths\":{\"%s\":{\"username\":\"%s\",\"password\":\"%s\",\"email\":\"%s\",\"auth\":\"%s\"}}}" .registry .username .password .email (printf "%s:%s" .username .password | b64enc) | b64enc }}
{{- end }}
{{- end }}

