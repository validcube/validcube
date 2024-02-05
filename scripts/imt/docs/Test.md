# `> Image_manipulation // Test`

| Test                  | Description            | Expected   |
| --------------------- | ---------------------- | ---------- |
| ::test_export_to_webp | Test exporting to webp | File exist |

## TestDeveloperExperience
Testing the experience of the user using the script

| Test                                        | Description                                     | Expected     |
| ------------------------------------------- | ----------------------------------------------- | ------------ |
| TestDeveloperExperience::test_create_folder | Test creating input/output folder               | Folder exist |
| TestDeveloperExperience::test_process       | Test converting input to output in PNG and WEBP | File exist   |

## TestAddMargin
Test adding margin to the test picture

| Test                                    | Description                                | Expected     |
| --------------------------------------- | ------------------------------------------ | ------------ |
| TestAddMargin::test_add_margin_negative | Test if the function allow negative number | ValueError   |
| TestAddMargin::test_add_margin_50       | Test adding 50 margins                     | Correct size |
| TestAddMargin::test_add_margin_100      | Test adding 100 margins                    | Correct size |
| TestAddMargin::test_add_margin_1000     | Test adding 1000 margins                   | Correct size |

## TestRoundCorner
Test adding corner to the test picture

| Test                                  | Description                                  | Expected     |
| ------------------------------------- | -------------------------------------------- | ------------ |
| TestRoundCorner::test_corner_negative | Test if the function allow negative number   | ValueError   |
| TestRoundCorner::test_corner_precise  | Test adding very precise corner (i.e. 3.243) | Correct size |
| TestRoundCorner::test_corner_8        | Test adding 8px corner radius                | Correct size |
| TestRoundCorner::test_corner_16       | Test adding 16px corner radius               | Correct size |
| TestRoundCorner::test_corner_24       | Test adding 24px corner radius               | Correct size |
