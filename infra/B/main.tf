provider "google" {
  credentials = file("/home/moriyama/semiotic-pact-362508-4bb79c5c5d78.json")
  project     = "semiotic-pact-362508"
  region      = "us-west1"
}

resource "google_storage_bucket" "bucket" {
  name     = "my-terraform-bucket"
  location = "us-west1"
}

resource "google_storage_bucket_object" "object" {
  name   = "sample.txt"
  bucket = google_storage_bucket.bucket.name
  source = "/home/moriyama/sample.txt"
}