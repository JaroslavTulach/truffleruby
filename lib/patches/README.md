# Temporary patching system

Whenever a file is required e.g. `bundler/cli/exec` and there is a file under same path in this `patches` directory, 
the file in the `patches` directory is immediately required as well patching (redefining) to original behaviour.
 
-   The patching system is loaded in `post-boot.rb` only when rubygems are enabled.
-   The code handling the patching itself can be found in `lib/truffle/truffle/patching.rb`.
