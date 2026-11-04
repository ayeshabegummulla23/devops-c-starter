![](https://nextwork.ai/ecstatic_purple_daring_surinam_cherry/uploads/d695935d-8372-4b16-8a7b-e69abc8284c0_x7tzo98a)

## Committing to Automated Feedback

### The purpose of the CI pipeline

In this project, I'm going to build the python calculator protected by three automated systems. So that The Github actions will check it an hosted linux runner after every push.

## Preparing a Reproducible Python Workspace

### Setting up an isolated development environment

In this step, We are preparing a predictable local workspace: checking Python 3.15.2, setting the global Git identity, and creating a virtual environment with pytest 9.2.0 installed.

![Preparing a Reproducible Python Workspace](https://nextwork.ai/ecstatic_purple_daring_surinam_cherry/uploads/d695935d-8372-4b16-8a7b-e69abc8284c0_3libaci5)

### Why dependency isolation matters

The virtual environment keeps this project’s packages separate from your computer’s main Python and from other projects.Think of it as a lunchbox for each project. Everything the project needs goes in its own box, so nothing gets mixed up.

## Building and Testing the Calculator Locally

### Creating a tested Python module

In this step, I'm going to build the calculator module and  the three tests that will protect the calculator's behavior.so,that i can prove the local baseline with one green pytest run.

### Predicting calculator behavior

I expect multiply(3, 4) to return 12. I expect is\_even(8) to return True.

![Building and Testing the Calculator Locally](https://nextwork.ai/ecstatic_purple_daring_surinam_cherry/uploads/d695935d-8372-4b16-8a7b-e69abc8284c0_z05eld0c)

## Automating Tests and Proving CI Catches Defects

### Connecting pytest to GitHub Actions

Running tests on my laptop only helps if you remember to do it, and people forget. GitHub Actions fixes this by running your tests automatically every time you push code to GitHub. You write the steps in a file called ci.yml. When you push, GitHub gets a fresh Linux computer, downloads your code, installs the packages, and runs pytest. If all tests pass, the run turns green. If any test fails, it turns red. First you publish the correct code, so you know the pipeline passes when everything is right. Then you break the code on purpose by changing a \* b to a + b. The tests fail and the run turns red. This proves the pipeline can catch mistakes automatically.

### Verifying the first successful workflow

The first green run proves that all the three test passes on the linux runner. because the automated safety is live and every new push now pass the same test .

![Diagnosing a Failed Build and Restoring Green](https://nextwork.ai/ecstatic_purple_daring_surinam_cherry/uploads/d695935d-8372-4b16-8a7b-e69abc8284c0_vzuw5f04)

## Diagnosing a Failed Build and Restoring Green

### Using CI evidence to guide the repair

In this step, i am diagnosing the failed multiplication tests from the workflow log, fixing multiply() so it returns a \* b, verifying locally with pytest, and pushing the fix to get a green GitHub Actions run.

### Tracing the failed multiply assertion

The pytest log showed that test\_multiply\_positive\_numbers received 7 instead of the expected 12, and test\_multiply\_negative\_number received 1 instead of the expected -6. Both wrong results are sums (3 + 4 = 7 and -2 + 3 = 1), while is\_even still passed. This showed that multiply() was using return a + b instead of return a \* b.

![Automating Tests and Proving CI Catches Defects](https://nextwork.ai/ecstatic_purple_daring_surinam_cherry/uploads/d695935d-8372-4b16-8a7b-e69abc8284c0_n8rje9m9)

## Validating Compatibility Across Python Versions

### How matrix testing strengthens CI coverage

In this project extension, I learned that matrix testing  matrix runs the same pytest suite on Python 3.13, 3.14, and 3.15 as three parallel jobs. Each job reports its own result, so CI shows exactly which Python versions are compatible with the code, instead of testing only one version.

## Reflecting on My CI Foundations

### Tools and concepts applied

In this project I learnt how to build a Python CI pipeline. I set up a virtual environment and Git, wrote a small calculator with pytest tests, and used GitHub Actions to run those tests automatically on a hosted Linux runner after every push. I introduced a bug on purpose and saw the pipeline turn red, then used the pytest log to find that multiply() returned sums (7 instead of 12, and 1 instead of -6). I fixed it to a \* b, checked it locally, and pushed to get a green run again. I also learnt how a matrix tests several Python versions in parallel to check compatibility. Overall, I learnt that CI catches mistakes automatically and gives clear evidence for fixing them.

### Project experience and challenges

t took me about 3 hours in total. The coding and testing were quick, but I spent extra time on setup and fixing Git errors like the rejected push.

### Next steps in my DevOps learning

Thanks for doing this project!\
I did this project today to learn how to build a Python CI pipeline with GitHub Actions that automatically tests my code and catches bugs. Another skill I want to learn is how to deploy an app automatically (CD), so code that passes the tests goes live by itself.
