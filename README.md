# pwhash
Recreating a password login system using sha256, hashes and salt

<h2>Proof of Concept</h2>

Recreates a standard sha256 encryption using a salt and a password to create a hash. In this example, there are four saved logins that entered in. After the logins are committed to memory, we wouldn't store the passwords in plain text anywhere.

*salt* - extra padding, unique to ensure no two passwords create the same hash. Stored with hash

*password* - must never be stored, never stored in plaintext.

*hash* - irreversible, stored in same place as salt
