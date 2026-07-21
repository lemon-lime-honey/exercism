package hamming

import "errors"

func Distance(a, b string) (int, error) {
    length := len(a)

    if length != len(b) {
        return 0, errors.New("")
    }

    result := 0

    for i := 0; i < length; i++ {
        if a[i] != b[i] {
            result++
        }
    }

    return result, nil
}
