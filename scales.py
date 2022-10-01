mode = {'ionian': 0, 'dorian': 1, 'phrygian': 2, 'lydian': 3, 'mixolydian': 4, 'aeolian': 5, 'locrian': 6}

keyOfC = [{'first': 'C', 'second': 'D', 'third': 'E', 'fourth': 'F', 'fifth': 'G', 'sixth': 'A', 'seventh': 'B'},
          {'first': 'D', 'second': 'E', 'third': 'F', 'fourth': 'G', 'fifth': 'A', 'sixth': 'B', 'seventh': 'C'},
          {'first': 'E', 'second': 'F', 'third': 'G', 'fourth': 'A', 'fifth': 'B', 'sixth': 'C', 'seventh': 'D'},
          {'first': 'F', 'second': 'G', 'third': 'A', 'fourth': 'B', 'fifth': 'C', 'sixth': 'D', 'seventh': 'E'},
          {'first': 'G', 'second': 'A', 'third': 'B', 'fourth': 'C', 'fifth': 'D', 'sixth': 'E', 'seventh': 'F'},
          {'first': 'A', 'second': 'B', 'third': 'C', 'fourth': 'D', 'fifth': 'E', 'sixth': 'F', 'seventh': 'G'},
          {'first': 'B', 'second': 'C', 'third': 'D', 'fourth': 'E', 'fifth': 'F', 'sixth': 'G', 'seventh': 'A'}]

keyOfDb = [{'first': 'Db', 'second': 'Eb', 'third': 'F', 'fourth': 'Gb', 'fifth': 'Ab', 'sixth': 'Bb', 'seventh': 'C'},
           {'first': 'Eb', 'second': 'F', 'third': 'Gb', 'fourth': 'Ab', 'fifth': 'Bb', 'sixth': 'C', 'seventh': 'Db'},
           {'first': 'F', 'second': 'Gb', 'third': 'Ab', 'fourth': 'Bb', 'fifth': 'C', 'sixth': 'Db', 'seventh': 'Eb'},
           {'first': 'Gb', 'second': 'Ab', 'third': 'Bb', 'fourth': 'C', 'fifth': 'Db', 'sixth': 'Eb', 'seventh': 'F'},
           {'first': 'Ab', 'second': 'Bb', 'third': 'C', 'fourth': 'Db', 'fifth': 'Eb', 'sixth': 'F', 'seventh': 'Gb'},
           {'first': 'Bb', 'second': 'C', 'third': 'Db', 'fourth': 'Eb', 'fifth': 'F', 'sixth': 'Gb', 'seventh': 'Ab'},
           {'first': 'C', 'second': 'Db', 'third': 'Eb', 'fourth': 'F', 'fifth': 'Gb', 'sixth': 'Ab', 'seventh': 'Bb'}]

keyOfD = [{'first': 'D', 'second': 'E', 'third': 'F#', 'fourth': 'G', 'fifth': 'A', 'sixth': 'B', 'seventh': 'C#'},
          {'first': 'E', 'second': 'F#', 'third': 'G', 'fourth': 'A', 'fifth': 'B', 'sixth': 'C#', 'seventh': 'D'},
          {'first': 'F#', 'second': 'G', 'third': 'A', 'fourth': 'B', 'fifth': 'C#', 'sixth': 'D', 'seventh': 'E'},
          {'first': 'G', 'second': 'A', 'third': 'B', 'fourth': 'C#', 'fifth': 'D', 'sixth': 'E', 'seventh': 'F#'},
          {'first': 'A', 'second': 'B', 'third': 'C#', 'fourth': 'D', 'fifth': 'E', 'sixth': 'F#', 'seventh': 'G'},
          {'first': 'B', 'second': 'C#', 'third': 'D', 'fourth': 'E', 'fifth': 'F#', 'sixth': 'G', 'seventh': 'A'},
          {'first': 'C#', 'second': 'D', 'third': 'E', 'fourth': 'F#', 'fifth': 'G', 'sixth': 'A', 'seventh': 'B'}]

keyOfEb = [{'first': 'Eb', 'second': 'F', 'third': 'G', 'fourth': 'Ab', 'fifth': 'Bb', 'sixth': 'C', 'seventh': 'D'},
           {'first': 'F', 'second': 'G', 'third': 'Ab', 'fourth': 'Bb', 'fifth': 'C', 'sixth': 'D', 'seventh': 'Eb'},
           {'first': 'G', 'second': 'Ab', 'third': 'Bb', 'fourth': 'C', 'fifth': 'D', 'sixth': 'Eb', 'seventh': 'F'},
           {'first': 'Ab', 'second': 'Bb', 'third': 'C', 'fourth': 'D', 'fifth': 'Eb', 'sixth': 'F', 'seventh': 'G'},
           {'first': 'Bb', 'second': 'C', 'third': 'D', 'fourth': 'Eb', 'fifth': 'F', 'sixth': 'G', 'seventh': 'Ab'},
           {'first': 'C', 'second': 'D', 'third': 'Eb', 'fourth': 'F', 'fifth': 'G', 'sixth': 'Ab', 'seventh': 'Bb'},
           {'first': 'D', 'second': 'Eb', 'third': 'F', 'fourth': 'G', 'fifth': 'Ab', 'sixth': 'Bb', 'seventh': 'C'}]

keyOfE = [{'first': 'E', 'second': 'F#', 'third': 'G#', 'fourth': 'A', 'fifth': 'B', 'sixth': 'C#', 'seventh': 'D#'},
          {'first': 'F#', 'second': 'G#', 'third': 'A', 'fourth': 'B', 'fifth': 'C#', 'sixth': 'D#', 'seventh': 'E'},
          {'first': 'G#', 'second': 'A', 'third': 'B', 'fourth': 'C#', 'fifth': 'D#', 'sixth': 'E', 'seventh': 'F#'},
          {'first': 'A', 'second': 'B', 'third': 'C#', 'fourth': 'D#', 'fifth': 'E', 'sixth': 'F#', 'seventh': 'G#'},
          {'first': 'B', 'second': 'C#', 'third': 'D#', 'fourth': 'E', 'fifth': 'F#', 'sixth': 'G#', 'seventh': 'A'},
          {'first': 'C#', 'second': 'D#', 'third': 'E', 'fourth': 'F#', 'fifth': 'G#', 'sixth': 'A', 'seventh': 'B'},
          {'first': 'D#', 'second': 'E', 'third': 'F#', 'fourth': 'G#', 'fifth': 'A', 'sixth': 'B', 'seventh': 'C#'}]

keyOfF = [{'first': 'E', 'second': 'F#', 'third': 'G#', 'fourth': 'A', 'fifth': 'B', 'sixth': 'C#', 'seventh': 'D#'},
          {'first': 'F#', 'second': 'G#', 'third': 'A', 'fourth': 'B', 'fifth': 'C#', 'sixth': 'D#', 'seventh': 'E'},
          {'first': 'G#', 'second': 'A', 'third': 'B', 'fourth': 'C#', 'fifth': 'D#', 'sixth': 'E', 'seventh': 'F#'},
          {'first': 'A', 'second': 'B', 'third': 'C#', 'fourth': 'D#', 'fifth': 'E', 'sixth': 'F#', 'seventh': 'G#'},
          {'first': 'B', 'second': 'C#', 'third': 'D#', 'fourth': 'E', 'fifth': 'F#', 'sixth': 'G#', 'seventh': 'A'},
          {'first': 'C#', 'second': 'D#', 'third': 'E', 'fourth': 'F#', 'fifth': 'G#', 'sixth': 'A', 'seventh': 'B'},
          {'first': 'D#', 'second': 'E', 'third': 'F#', 'fourth': 'G#', 'fifth': 'A', 'sixth': 'B', 'seventh': 'C#'}]

keyOfGb = [{'first': 'Gb', 'second': 'Ab', 'third': 'Bb', 'fourth': 'C', 'fifth': 'Db', 'sixth': 'Eb', 'seventh': 'F'},
          {'first': 'Ab', 'second': 'Bb', 'third': 'C', 'fourth': 'Db', 'fifth': 'Eb', 'sixth': 'F', 'seventh': 'Gb'},
          {'first': 'Bb', 'second': 'C', 'third': 'Db', 'fourth': 'Eb', 'fifth': 'F', 'sixth': 'Gb', 'seventh': 'Ab'},
          {'first': 'C', 'second': 'Db', 'third': 'Eb', 'fourth': 'F', 'fifth': 'Gb', 'sixth': 'Ab', 'seventh': 'Bb'},
          {'first': 'Db', 'second': 'Eb', 'third': 'F', 'fourth': 'Gb', 'fifth': 'Ab', 'sixth': 'Bb', 'seventh': 'C'},
          {'first': 'Eb', 'second': 'F', 'third': 'Gb', 'fourth': 'Ab', 'fifth': 'Bb', 'sixth': 'C', 'seventh': 'Db'},
          {'first': 'F', 'second': 'Gb', 'third': 'Ab', 'fourth': 'Bb', 'fifth': 'C', 'sixth': 'Db', 'seventh': 'Eb'}]

keyOfG = [{'first': 'G', 'second': 'A', 'third': 'B', 'fourth': 'C', 'fifth': 'D', 'sixth': 'E', 'seventh': 'F#'},
          {'first': 'A', 'second': 'B', 'third': 'C', 'fourth': 'D', 'fifth': 'E', 'sixth': 'F#', 'seventh': 'G'},
          {'first': 'B', 'second': 'C', 'third': 'D', 'fourth': 'E', 'fifth': 'F#', 'sixth': 'G', 'seventh': 'A'},
          {'first': 'C', 'second': 'D', 'third': 'E', 'fourth': 'F#', 'fifth': 'G', 'sixth': 'A', 'seventh': 'B'},
          {'first': 'D', 'second': 'E', 'third': 'F#', 'fourth': 'G', 'fifth': 'A', 'sixth': 'B', 'seventh': 'C'},
          {'first': 'E', 'second': 'F#', 'third': 'G', 'fourth': 'A', 'fifth': 'B', 'sixth': 'C', 'seventh': 'D'},
          {'first': 'F#', 'second': 'G', 'third': 'A', 'fourth': 'B', 'fifth': 'C', 'sixth': 'D', 'seventh': 'E'}]

keyOfAb = [{'first': 'Ab', 'second': 'Bb', 'third': 'C', 'fourth': 'Db', 'fifth': 'Eb', 'sixth': 'F', 'seventh': 'G'},
          {'first': 'Bb', 'second': 'C', 'third': 'Db', 'fourth': 'Eb', 'fifth': 'F', 'sixth': 'G', 'seventh': 'Ab'},
          {'first': 'C', 'second': 'Db', 'third': 'Eb', 'fourth': 'F', 'fifth': 'G', 'sixth': 'Ab', 'seventh': 'Bb'},
          {'first': 'Db', 'second': 'Eb', 'third': 'F', 'fourth': 'G', 'fifth': 'Ab', 'sixth': 'Bb', 'seventh': 'C'},
          {'first': 'Eb', 'second': 'F', 'third': 'G', 'fourth': 'Ab', 'fifth': 'Bb', 'sixth': 'C', 'seventh': 'Db'},
          {'first': 'F', 'second': 'G', 'third': 'Ab', 'fourth': 'Bb', 'fifth': 'C', 'sixth': 'Db', 'seventh': 'Eb'},
          {'first': 'G', 'second': 'Ab', 'third': 'Bb', 'fourth': 'C', 'fifth': 'Db', 'sixth': 'Eb', 'seventh': 'F'}]

keyOfA = [{'first': 'A', 'second': 'B', 'third': 'C#', 'fourth': 'D', 'fifth': 'E', 'sixth': 'F#', 'seventh': 'G#'},
          {'first': 'B', 'second': 'C#', 'third': 'D', 'fourth': 'E', 'fifth': 'F#', 'sixth': 'G#', 'seventh': 'A'},
          {'first': 'C#', 'second': 'D', 'third': 'E', 'fourth': 'F#', 'fifth': 'G#', 'sixth': 'A', 'seventh': 'B'},
          {'first': 'D', 'second': 'E', 'third': 'F#', 'fourth': 'G#', 'fifth': 'A', 'sixth': 'B', 'seventh': 'C#'},
          {'first': 'E', 'second': 'F#', 'third': 'G#', 'fourth': 'A', 'fifth': 'B', 'sixth': 'C#', 'seventh': 'D'},
          {'first': 'F#', 'second': 'G#', 'third': 'A', 'fourth': 'B', 'fifth': 'C#', 'sixth': 'D', 'seventh': 'E'},
          {'first': 'G#', 'second': 'A', 'third': 'B', 'fourth': 'C#', 'fifth': 'D', 'sixth': 'E', 'seventh': 'F#'}]

keyOfBb = [{'first': 'Bb', 'second': 'C', 'third': 'D', 'fourth': 'Eb', 'fifth': 'F', 'sixth': 'G', 'seventh': 'A'},
          {'first': 'C', 'second': 'D', 'third': 'Eb', 'fourth': 'F', 'fifth': 'G', 'sixth': 'A', 'seventh': 'Bb'},
          {'first': 'D', 'second': 'Eb', 'third': 'F', 'fourth': 'G', 'fifth': 'A', 'sixth': 'Bb', 'seventh': 'C'},
          {'first': 'Eb', 'second': 'F', 'third': 'G', 'fourth': 'A', 'fifth': 'Bb', 'sixth': 'C', 'seventh': 'D'},
          {'first': 'F', 'second': 'G', 'third': 'A', 'fourth': 'Bb', 'fifth': 'C', 'sixth': 'D', 'seventh': 'Eb'},
          {'first': 'G', 'second': 'A', 'third': 'Bb', 'fourth': 'C', 'fifth': 'D', 'sixth': 'Eb', 'seventh': 'F'},
          {'first': 'A', 'second': 'Bb', 'third': 'C', 'fourth': 'D', 'fifth': 'Eb', 'sixth': 'F', 'seventh': 'G'}]

keyOfB = [{'first': 'B', 'second': 'C#', 'third': 'D#', 'fourth': 'E', 'fifth': 'F#', 'sixth': 'G#', 'seventh': 'A#'},
          {'first': 'C#', 'second': 'D#', 'third': 'E', 'fourth': 'F#', 'fifth': 'G#', 'sixth': 'A#', 'seventh': 'B'},
          {'first': 'D#', 'second': 'E', 'third': 'F#', 'fourth': 'G#', 'fifth': 'A#', 'sixth': 'B', 'seventh': 'C#'},
          {'first': 'E', 'second': 'F#', 'third': 'G#', 'fourth': 'A#', 'fifth': 'B', 'sixth': 'C#', 'seventh': 'D#'},
          {'first': 'F#', 'second': 'G#', 'third': 'A#', 'fourth': 'B', 'fifth': 'C#', 'sixth': 'D#', 'seventh': 'E'},
          {'first': 'G#', 'second': 'A#', 'third': 'B', 'fourth': 'C#', 'fifth': 'D#', 'sixth': 'E', 'seventh': 'F#'},
          {'first': 'A#', 'second': 'B', 'third': 'C#', 'fourth': 'D#', 'fifth': 'E', 'sixth': 'F#', 'seventh': 'G#'}]

keys = [keyOfC, keyOfDb, keyOfD, keyOfEb, keyOfE, keyOfF, keyOfGb, keyOfG, keyOfAb, keyOfA, keyOfBb, keyOfB]
