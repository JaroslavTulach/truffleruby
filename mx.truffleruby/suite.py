# Copyright (c) 2016 Oracle and/or its affiliates. All rights reserved. This
# code is released under a tri EPL/GPL/LGPL license. You can use it,
# redistribute it and/or modify it under the terms of the:
#
# Eclipse Public License version 1.0
# GNU General Public License version 2
# GNU Lesser General Public License version 2.1

def mavenLib(mavenDep, sha1, sourceSha1, mavenLibLicense):
    components = mavenDep.split(':')
    if len(components) == 3:
        groupId, artifactId, version = components
        native = None
    else:
        groupId, artifactId, version, native = components
    if native:
        args = (groupId.replace('.', '/'), artifactId, version, artifactId, version, native)
        base = "https://search.maven.org/remotecontent?filepath=%s/%s/%s/%s-%s-%s" % args
    else:
        args = (groupId.replace('.', '/'), artifactId, version, artifactId, version)
        base = "https://search.maven.org/remotecontent?filepath=%s/%s/%s/%s-%s" % args
    url = base + ".jar"
    sourceUrl = base + '-sources.jar'
    description = {
        "urls": [url],
        "sha1": sha1,
        "maven": {
            "groupId": groupId,
            "artifactId": artifactId,
            "version": version,
        },
        "license": mavenLibLicense
    }
    if sourceSha1:
        description["sourceUrls"] = [sourceUrl]
        description["sourceSha1"] = sourceSha1
    return description

suite = {
    "mxversion": "5.80.2",
    "name": "truffleruby",

    "imports": {
        "suites": [
            {
                "name": "truffle",
                # Must be the same as in truffle/pom.xml (except for the -SNAPSHOT part only in pom.xml, and there we can use a release name)
                "version": "c02973969fb144b533ae0e53187674cb04c2aacc",
                "urls": [
                    {"url": "https://github.com/graalvm/truffle.git", "kind": "git"},
                    {"url": "https://curio.ssw.jku.at/nexus/content/repositories/snapshots", "kind": "binary"},
                ]
            },
        ],
    },

    "licenses": {
        "EPL-1.0": {
            "name": "Eclipse Public License 1.0",
            "url": "https://opensource.org/licenses/EPL-1.0",
        },
        "BSD-simplified" : {
          "name" : "Simplified BSD License (2-clause BSD license)",
          "url" : "http://opensource.org/licenses/BSD-2-Clause"
        },
        "MIT" : {
          "name" : "MIT License",
          "url" : "http://opensource.org/licenses/MIT"
        },
        "Apache-2.0" : {
          "name" : "Apache License 2.0",
          "url" : "https://opensource.org/licenses/Apache-2.0"
        },
        "GPLv2" : {
          "name" : "GNU General Public License, version 2",
          "url" : "http://www.gnu.org/licenses/old-licenses/gpl-2.0.en.html"
        },
        "zlib" : {
          "name" : "The zlib License",
          "url" : "https://opensource.org/licenses/zlib"
        },
    },

    "repositories" : {
         "truffleruby-binary-snapshots" : {
             "url" : "https://curio.ssw.jku.at/nexus/content/repositories/snapshots",
             "licenses" : ["EPL-1.0", "BSD-simplified", "BSD-new", "MIT", "Apache-2.0", "GPLv2", "LGPLv21", "zlib"]
          },
     },

    "libraries": {

        # ------------- Libraries -------------

        "ASM": mavenLib(
          "org.ow2.asm:asm:5.0.4",
          "0da08b8cce7bbf903602a25a3a163ae252435795",
          None,
          "BSD-new"),

        "JNR_POSIX": mavenLib(
          "com.github.jnr:jnr-posix:3.0.37",
          "35a85096ba99b478a92f05693abd236988d47c6d",
          "7a80c45c80033774e1c3f6816ee68f3f8fca0aa5",
          "EPL-1.0"),

        "JNR_CONSTANTS": mavenLib(
          "com.github.jnr:jnr-constants:0.9.6",
          "84955256aa28919f12b6c7c9437ed65d814a3c0c",
          "5579ab41c687085e714fc330536ec4dda3350b08",
          "Apache-2.0"),

        "JNR_FFI": mavenLib(
          "com.github.jnr:jnr-ffi:2.1.3",
          "eae1dd4a7454ddbf000bb95f5c1912894221f5e1",
          "fcd823ddc2d1d17dca8ea63ba680d6c50f388e0b",
          "Apache-2.0"),

        "JFFI": mavenLib(
          "com.github.jnr:jffi:1.2.13",
          "8926bd0b2d0e9a46e7607eb7866356845c7df9a2",
          "691ec868b9569092687553a8099a28f71f175097",
          "Apache-2.0"),

        "JFFI_NATIVE": mavenLib(
          "com.github.jnr:jffi:1.2.13:native",
          "c4b81ddacd1e94a73780aa6e4e8b9d2945d5eb4c",
          None,
          ["Apache-2.0", "MIT"]),

        "SNAKEYAML": mavenLib(
            "org.yaml:snakeyaml:1.14",
            "c2df91929ed06a25001939929bff5120e0ea3fd4",
            "4c6bcedc3efa772a5ae1c2fd01efee8e4d15edac",
            "Apache-2.0"),

        "JONI": mavenLib(
            "org.jruby.joni:joni:2.1.11",
            "655cc3aba1bc9dbdd653f28937bec16f3e9c4cec",
            "2982d6beb2f8fabe5ac5cc9dec6b4d6a9ffeedb1",
            "MIT"),

        "JCODINGS": mavenLib(
            "org.jruby.jcodings:jcodings:1.0.18",
            "e2c76a19f00128bb1806207e2989139bfb45f49d",
            "201985f0f15af95f03494ab9ef0400e849090d6c",
            "MIT"),

    },

    "projects": {

        # ------------- Projects -------------

        "truffleruby": {
            "dir": "truffleruby/src/main",
            "sourceDirs": ["java"],
            "dependencies": [
                "truffle:TRUFFLE_API",
                "truffle:TRUFFLE_DEBUG",
                "truffle:JLINE",
                "ASM",
                "JNR_POSIX",
                "JNR_CONSTANTS",
                "JNR_FFI",
                "JFFI",
                "JFFI_NATIVE",
                "SNAKEYAML",
                "JONI",
                "JCODINGS",
            ],
            "annotationProcessors": ["truffle:TRUFFLE_DSL_PROCESSOR"],
            "javaCompliance": "1.8",
            "workingSets": "TruffleRuby",
            "checkPackagePrefix": "false",
            "license": ["EPL-1.0", "BSD-new", "BSD-simplified", "MIT", "Apache-2.0"],
        },

        "truffleruby-core": {
            "class": "ArchiveProject",
            "outputDir": "truffleruby/src/main/ruby",
            "prefix": "truffleruby",
            "license": ["EPL-1.0", "BSD-new"],
        },

        "truffleruby-test": {
            "dir": "truffleruby/src/test",
            "sourceDirs": ["java"],
            "dependencies": [
                "truffleruby",
                "truffle:TRUFFLE_TCK",
                "mx:JUNIT",
            ],
            "javaCompliance": "1.8",
            "checkPackagePrefix": "false",
            "license": "EPL-1.0",
        },

        "truffleruby-test-ruby": {
            "class": "ArchiveProject",
            "outputDir": "truffleruby/src/test/ruby",
            "prefix": "src/test/ruby",
            "license": "EPL-1.0",
        },

        "truffleruby-lib": {
            "class": "ArchiveProject",
            "outputDir": "lib",
            "prefix": "lib",
            "license": ["EPL-1.0", "MIT", "BSD-simplified", "GPLv2", "LGPLv21", "zlib"],
        },

        "truffleruby-bin": {
            "class": "ArchiveProject",
            "outputDir": "bin",
            "prefix": "bin",
            "license": ["EPL-1.0", "GPLv2", "LGPLv21"],
        },

        "truffleruby-doc": {
            "class": "TruffleRubyDocsProject",
            "outputDir": "",
            "prefix": "",
        },
    },

    "distributions": {

        # ------------- Distributions -------------

        "TRUFFLERUBY": {
            "mainClass": "org.truffleruby.Main",
            "dependencies": [
                "truffleruby",
                "truffleruby-core",
            ],
            "distDependencies": [
                "truffle:TRUFFLE_API",
                "truffle:TRUFFLE_DEBUG",
            ],
            "description": "TruffleRuby",
            "license": ["EPL-1.0", "BSD-new", "BSD-simplified", "MIT", "Apache-2.0"],
        },

        # Set of extra files to extract to run Ruby
        "TRUFFLERUBY-ZIP": {
            "native": True, # Not Java
            "relpath": True,
            "dependencies": [
                "truffleruby-bin",
                "truffleruby-lib",
                "truffleruby-doc",
            ],
            "description": "TruffleRuby libraries",
            "license": ["EPL-1.0", "MIT", "BSD-simplified", "GPLv2", "LGPLv21", "zlib"],
        },

        "TRUFFLERUBY-TEST": {
            "dependencies": [
                "truffleruby-test",
                "truffleruby-test-ruby",
            ],
            "exclude" : [
                "mx:HAMCREST",
                "mx:JUNIT"
            ],
            "distDependencies": [
                "TRUFFLERUBY",
                "truffle:TRUFFLE_TCK"
            ],
            "license": "EPL-1.0",
        },
    },
}
